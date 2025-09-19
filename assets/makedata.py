import datetime

import sys, os, django, traceback
sys.path.append(os.path.abspath("."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs3550.settings")
try:
    django.setup()
except:
    traceback.print_exc()
    print("""Django setup failed. Make sure to run this from your repository""")
    exit(1)

import re, hashlib
from django.utils import timezone
from django.core.files.base import File
from dishbook.models import User, Recipe, Step, Ingredient, Tag, Profile

def asset(name, mode="r"):
    file_dir = os.path.dirname(__file__)
    photo_path = os.path.join(file_dir, name)
    if os.path.exists(photo_path) and os.path.isfile(photo_path):
        kwargs = {} if "b" in mode else { "encoding": "utf8"}
        return open(photo_path, mode, **kwargs)
    else:
        print(f"Could not find `{name}`; make sure you are running this correctly.")
        sys.exit(1)

def check_has_data():
    return User.objects.all().count() or \
        Recipe.objects.all().count() or \
        Step.objects.all().count() or \
        Ingredient.objects.all().count() or \
        Tag.objects.all().count()

def create_users():
    prof = User.objects.create_superuser(
        "pavpan", "pavpan@cs.utah.edu", "pavpan",
        first_name="Prof.", last_name="Panchekha",
    )

    u1 = User.objects.create_user(
        "a", "a@cs.utah.edu", "a",
        first_name="Alice", last_name="Apron",
    )
    u2 = User.objects.create_user(
        "b", "b@cs.utah.edu", "b",
        first_name="Ben", last_name="Braiser",
    )
    u3 = User.objects.create_user(
        "c", "c@cs.utah.edu", "c",
        first_name="Cathy", last_name="Colander",
    )
    u4 = User.objects.create_user(
        "d", "d@cs.utah.edu", "d",
        first_name="Dan", last_name="Doughkneeder",
    )

    Profile.objects.create(user=u1)
    Profile.objects.create(user=u2)
    Profile.objects.create(user=u3)
    Profile.objects.create(user=u4)

    with asset("ben-braiser.png", "rb") as f:
        u2.profile.photo.save("ben-braiser.png", File(f), save=True)

    u2.profile.bio = """
    I'm a home cook who loves bold flavors and simple techniques. Most of
    my recipes come from weeknight dinners, backyard grilling, and a few
    kitchen experiments that turned out better than expected. When I'm not
    cooking, I'm usually testing new spice blends or perfecting something
    in my cast iron."""
    u2.profile.save()

    u3.profile.bio = """
    Passionate home cook who loves experimenting with family recipes and
    fresh seasonal ingredients. Always excited to share new dishes, learn
    from others, and swap kitchen tips."""
    u3.profile.save()

    return u1, u2, u3, u4

# Note, this code is pretty ugly and is just intended to load recipes
# from a "pre-baked" text file. Fields like author and is_public are
# chosen randomly.
def parse_recipe(lines, author):
    title = re.match(r'^#\s*(.*)', lines[0]).group(1).strip()
    
    # Group lines into buckets
    metadata = {}
    description = ""
    step_ingredient_lines = []
    
    for line in lines[1:]:  # Skip title line
        line = line.strip()
        if not line:  # Whitespace only - ignore
            continue
        elif ':' in line and line.split(':', 1)[0].isalpha():
            key, value = line.split(":", 1)
            metadata[key.casefold()] = value.strip()
        elif line[0].isalpha():  # Description (starts with letter)
            description += " " + line
        elif line[0].isdigit() or line[0].isspace() or line.startswith('-') or line.startswith('–'):  # Steps/ingredients
            step_ingredient_lines.append(line)
    
    # Create Recipe with author
    recipe = Recipe.objects.create(
        title=title,
        author=author,
        description=description,
        prep_time_minutes=int(metadata['prep'].split()[0]),
        cook_time_minutes=int(metadata['cook'].split()[0]),
        serves=int(metadata['serves']),
    )

    # Set tags
    recipe.tags.set([
        Tag.objects.get_or_create(name=tag.removeprefix("#"))[0]
        for tag in metadata['tags'].split()
    ])

    if "photo" in metadata:
        with asset(metadata["photo"], "rb") as f:
            recipe.photo.save(metadata["photo"], File(f), save=True)
    
    # Default is_public based on title hash
    #h = hashlib.md5(title.encode('utf-8')).hexdigest()
    #num = int(h[8], 16)
    #recipe.is_public = num >= 10
    #recipe.save()
    
    # Parse steps and ingredients
    i = 0
    step_pattern = re.compile(r'^(\d+)\.\s*(.*)')
    ing_pattern = re.compile(r'^\s*[-–]\s*(.*)')
    
    while i < len(step_ingredient_lines):
        line = step_ingredient_lines[i]
        step_match = step_pattern.match(line)
        if step_match:
            order = int(step_match.group(1))
            desc_parts = [step_match.group(2).strip()]
            i += 1
            # Gather wrapped description lines until next ingredient or step
            while i < len(step_ingredient_lines) and not step_pattern.match(step_ingredient_lines[i]) and not ing_pattern.match(step_ingredient_lines[i]):
                desc_parts.append(step_ingredient_lines[i].strip())
                i += 1
            step = Step.objects.create(
                recipe=recipe,
                order=order,
                description=' '.join(desc_parts)
            )
            # Collect ingredients for this step
            while i < len(step_ingredient_lines):
                ing_match = ing_pattern.match(step_ingredient_lines[i])
                if not ing_match:
                    break
                ingr_text = ing_match.group(1).strip()
                m = re.match(r'(?P<amount>\d*\.?\d+)\s+(?P<unit>\w+)\s+(?P<name>.*)', ingr_text)
                if m:
                    amount = float(m.group('amount'))
                    unit = m.group('unit')
                    name = m.group('name')
                else:
                    amount, unit, name = 0, '', ingr_text
                Ingredient.objects.create(
                    amount=amount,
                    unit=unit,
                    name=name,
                    step=step
                )
                i += 1
        else:
            i += 1
    return recipe

def load_file(file_name):
    with asset(file_name, 'r') as f:
        return re.split(r'(?m)^(?=#\s)', f.read())

def parse_file(blocks, authors):
    """
    authors: list of User instances
    """
    parsed = []

    # Parse all recipes, assigning authors deterministically
    for idx, block in enumerate(blocks):
        if not block.strip():
            continue
        # choose author based on block index
        author = authors[idx % len(authors)]
        lines = block.strip().splitlines()
        recipe = parse_recipe(lines, author)
        parsed.append(recipe)

    # Mark copied_from relationships and enforce publication rules
    for recipe in parsed:
        for prev in parsed:
            if prev != recipe and prev.title in recipe.title:
                # don't allow copying self
                if recipe.author != prev.author:
                    recipe.copied_from = prev
                    recipe.save()
                    #prev.is_public = True
                    #prev.save()
                break

    # Feature only the three specific recipes
    for recipe in parsed:
        recipe.featured_on = None
        recipe.save()
    to_feature = parsed[1], parsed[17], parsed[24], parsed[38]
    base = datetime.date(2025, 1, 1)
    for r in to_feature:
        # reproducible date based on hash
        h = hashlib.md5(r.title.encode('utf-8')).hexdigest()
        num = int(h[:8], 16)
        days = num % 365
        hour = num % 24
        feat_date = base + datetime.timedelta(days=days)
        feat_dt = datetime.datetime.combine(feat_date, datetime.time(hour=hour, minute=0))
        r.featured_on = timezone.make_aware(feat_dt)
        #r.is_public = True
        r.save()

    return parsed

def print_recipe_tree(recipe, prefix="- "):
    print(prefix + recipe.title)
    for child in recipe.copies.all():
        print_recipe_tree(child, "  " + prefix)

if __name__ == "__main__":
    if check_has_data():
        print("""It looks you've already run the makedata.py script.
If you've changed the model and want to rerun the script, run:
        
    python3 manage.py makemigrations
    rm db.sqlite3
    python3 manage.py migrate
    python3 makedata.py
""")
        exit(1)
    with django.db.transaction.atomic():
        users = create_users()
        blocks = load_file("data.txt")
        recipes = parse_file(blocks, users)
        print("Loaded recipes:\n")
        for recipe in recipes:
            if not recipe.copied_from:
                print_recipe_tree(recipe)

