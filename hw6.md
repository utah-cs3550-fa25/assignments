CS 3550 Assignment 6 (JavaScript)
==================================

**Status**: Final \
**Due**: Phase 1 due **14 Nov**, Phase 2--5 due **21 Nov**

About
-----

In this assignment, you'll use JavaScript to add a variety of
convenient user interactions to the recipe application. Specifically,
you will:

- Show and hide passwords on the login form
- Update computed values on recipe edit page
- Search recipes as the user types

The assignment is due Friday, 21 November before midnight. The
course's normal extension policy applies.



Phase 1: Adding JavaScript
--------------------------

Create a file named `main.js` in your `static/` directory. Add the
following contents to it:

    console.log("Hello", document.title);
    
This writes to the browser debugging console on load.

Now edit your `header.html` template (which should be included on all
web pages) and add the following line to it:

    <script src="/static/main.js" type="module"></script>

Note that we are including the script as a "JavaScript module", as
discussed in class. Modules (often called "ES6 modules" after the
version of JavaScript where they were introduced) are a relatively new
feature and you'll see a lot of older JavaScript tutorials not use
them, but they opt you into better defaults and are a good idea.

Run your server and visit a page. (Since you edited `header.html`, any
page should do.) Open the browser developer console. You should see
the text "Hello" and then the tab title appear. If it does, commit all
of your changes and confirm that more of the autotester is now
passing. If it does not, get help.



Phase 2: Viewing passwords
--------------------------

Make sure your `main.js` file is included from your `/login` page;
this should already be happening, but it's good to make sure. We want
to implement a "view password" checkbox to allow people to see their
password as they type it. This is especially important on mobile,
because it's easy to make typos using the on-screen keyboard.

Start by adding a checkbox to the login page. Make sure to give it a
label, and make sure it looks normal on the web page (no bizarre
whitespace or multiple rows for the checkbox and its label). Do *not*
give the checkbox a `name` attribute; we do not want the checkbox
submitted with the form. Do give the checkbox a unique `id`.

In your `main.js` file, select the element with that `id`. Recall that
the `main.js` code runs on every page on the recipe site, but only the
login page will have an element with this `id`. So the rest of the
show-password handling code should only run when this element is present.
Also select the password input element; it might be useful to give it
an `id` as well, but don't change its `name` or other attributes.

More generally, to implement this feature, and every other JavaScript
feature on this page, we will *only write JavaScript in `main.js`*. Do
not create other JavaScript files or write inline JavaScript in
individual templates.

Once you've selected the checkbox element in JavaScript, attach an
event handler to its `input` event. The `input` event is a more
convenient than `click` for two reasons. First, `input` occurs *after*
an input element changes its value, so by the time the event handler
runs, the checkbox's checked or unchecked state is already updated and
can be used. Second, `input` happens even if the input's state changes
via keyboard (like by tabbing to the input element and pressing the
space bar) instead of using the mouse.

In the event handler, read the `checked` attribute of the checkbox
element; if the checkbox is checked, set the password's `type` to
`text`, while if it's unchecked, set it to `password`.

Test this code. Make sure checking and un-checking the checkbox works
correctly. Make sure there are no exceptions or errors printed to the
developer console, on the login page or on any other pages.



Phase 3: Updating computed values
---------------------------------

Next, go to your `edit.html` page. On it, you should have a read-only
input box for the "total time" a recipe takes (meaning, its prep time
plus its cook time). It currently shows the total time for the recipe
when the page was loaded, which means that if you update the prep time
or cook time fields, the total time field doesn't change and becomes
out of date. We want to fix this.

In your `main.js` file, select the total time, cook time, and prep
time input fields. You might want to give them IDs or otherwise
distinguish them to make them easy to select. As in Phase 2, keep in
mind that the code you write will run on *all* of the pages on your
website, so be mindful of the fact that you might not select any
elements (in which case you're not on the edit page and your code
doesn't need to do anything).

Once you've selected all three elements, add event listeners to the
prep time and cook time input elements to update the value of the
total time input field any time the prep time or cook time inputs
change.

You can read or change the value of an input element using its `value`
field. However, *be careful*: the value of this field is a string.
JavaScript uses `+` for string concatenation as well as for
arithmetic, so you can end up with silly results like `"20" + "35"`
(the addition of two strings) evaluating to `"2035"` (their
concatenation). Mixed-type operations (like adding an integer to a
string) cause "type coercion" which probably won't give you the right
result either. So make sure to convert *all* arguments from strings to
numbers before you do arithmetic on them. You can convert a string to
a number in JavaScript using a prefix `+` operation, like in `+"25"`.

The edit page also has a list of ingredients (on the left, next to the
list of steps). This list of ingredients can *also* get out of sync
with the actual ingredients that the user has entered in below the
list of steps.

Select all of the ingredients input entries on the page. Since there's
more than one, adding IDs won't help, but you can write a more
complicated CSS selector or add classes to selects all of the
ingredient input fields (name, unit, and amount) on the page. Add an
event handler to *each* of them. When any ingredient changes, read
*all* of the ingredients and reconstruct the ingredient list.

You can find details of how the ingredient list is constructed in
[Assignment 3](hw3.md). In short, the ingredient list should be sorted
by the first step where each ingredient appears. When an ingredient
appears in more than two steps, you should add the amounts if the
units are the same, but not if the units are different, and then show
something like "2 cups and 1 tbsp flour" in the ingredients list. This
will be mildly challenging, but you can consult your own
implementation of Assignment 3 for ideas.

To do this, you'll want to iterate over all of the ingredients entries
and build some kind of data structure. Then use this data structure to
generate the ingredients list. Note that, unlike Python, objects in
JavaScript aren't sorted by insertion order. So I recommend using a
dictionary *and* and array in this data structure for storing the
ingredients in the proper order.

Once you've built the proper data structure, you'll want to use it to
update the ingredients list. It's probably most convenient to do so
using the [`replaceChildren` method][mdn-replacechildren] on
`HTMLElement`, though you're also free to do it some other way. Make
sure to match the styling of the original ingredient list. When you
edit an ingredient name, unit, or amount, the changes should look
smooth, without large changes to the page.

[mdn-replacechildren]: https://developer.mozilla.org/en-US/docs/Web/API/Element/replaceChildren



Phase 4: Searching recipes
--------------------------

Finally, let's make as-you-type recipe search work on our recipe site.
To start with, let's make normal recipe search work, and then we'll
add as-you-type speed in Phase 5.

There are two search forms on our website: one on `search.html`, and
one in your `header.html`. Make sure both submit to `/s` using a `GET`
request. A `GET` request is appropriate, because a search form doesn't
change the database in any way. Inside both search forms, make sure
the search input has `type="search"` (it may show a little magnifying
glass in your browser) and has a name of `q` (short for "query").

Go to your `search` controller in `views.py`. Edit the controller to
retrieve the `q` value from the GET parameters and pass that query
through to the `search.html` template. Use that to set the initial
value of the search input.

Test that everything works. Go to the index page and type a search
query into the search box in the page header. Press the "Search"
button. You should now be on the search page, and the search form in
the middle of the page should show your search query. Edit that query
and press "Enter"; you should now see your updated query.

Now let's implement search. At the moment, your `search` controller
should show all public recipes, plus private recipes from the current
user. When we search something, we want to show a _subset_ of that.
Specifically, a search query corresponds to a space-separated list of
"keywords". For example, the search query `taco onion` has two
keywords: `taco` and `onion`.

We will implement three types of keywords:

- `tag:name` will take only recipes with a certain tag
- `variation:ID` will only show recipes copied from given recipe ID
- `other` will only show recipes that contain the keyword in the title

Conceptually, each keyword *reduces* the set of results. An empty
search query has a lot of results; adding `taco` reduces the result
set; adding `onion` reduces it further.

Implement searching in your `search` controller. Start with a query
that selects all (public or current-user) recipes. Don't execute the
query, though---we'll now refine this query using the keywords. Then
split user input into keywords and iterate through them. For each
keyword, add an extra `filter` step to the search query. The exact
`filter` step depends on the keyword type, as in the list above. You
might find the Python `startswith` and `removeprefix` string functions
useful. When checking if the recipe title contains a given keyword,
use the `icontains` function, which checks string containment in a
case-insensitive way.

If you'd like, as an extra challenge, you can make `other` keywords
search over not only the recipe title but also the description, step
descriptions, and ingredient names. You'll need to use `Q` objects for
that.

Once you've iterated over all of the keywords, you should now have a
Django query that selects only matching recipes. Pass that to the
`search.html` template.

Test that you can search for things like `potatoes` and see only
recipes that mention potatoes in the title. Also test `tag:comfort`
and `variation:1`. All of those queries should return something. If
you see a recipe appear more than once, you've probably done something
wrong (unless you're doing the extra challenge, then it's expected),
but you can try to add a `distinct` and see if that helps.

Once everything is working, go to your `recipe.html`, `edit.html`, and
`card.html` templates, each of which should show a list of tags. Make
each tag link to `/s?q=tag:TAG`. This way, clicking on a tag name
should show all of the recipes with that tag. Furthermore, in
`recipe.html` and `edit.html`, you should (for some recipes) output a
link that says something like "3 variations". Link that text to
`/s?q=variation:ID`, so that clicking on that text shows all of the
variations. Test that on, say, the "Funeral Potatoes" recipe
(`/recipe/1`): the recipe page should say "1 variation" and clicking
on that link should show a search page with 1 result (for "Funeral
Potatoes with Parmesan").



Phase 5: Search as you type
---------------------------

Phase 4, on search, didn't actually involve any JavaScript, and the
search results only appeared when you finished typing and pressed
"Enter". But with JavaScript, we can make search "instant", with
as-you-type results.

This will require changes to both the front-end and the back-end.
Here's how it will work:

- JavaScript will listen to changes to the search bar
- Whenever there's a change, it will make a `fetch` request to a
  special `/api/s` URL.
- That endpoint will perform the search and return JSON describing the
  results
- JavaScript will then interpret that JSON to update the web page

Let's start with the backend. Create a new controller called
`search_api` and route `/api/s` to it. This controller will behave
almost the same as the normal `search` controller (you can move the
common part to a helper function if you'd like). However, whereas the
`search` controller returns a `render`ing of a template, the
`search_api` controller will construct a Python object like this:

```
{ "results": [
  {
    "id": 3,
    "title": "Green Jell-O with Pineapple and Carrots",
    "photo": "/recipe/3/photo",
    "tags": ["holiday", "utah"]
  }, ...
]}
```

Don't include the `photo` field for recipes with no photo.

Then, the controller will return that Python object, wrapped in a
`JsonResponse`, like this:

    def search_api(request):
        # ... compute the database query q
        results = []
        for recipe in q:
            # ... create an entry in `response` for the recipe
        return JsonResponse({ "results": results })

Test this in your browser: open `/api/s?q=potatoes` and make sure you
see correctly-formatted JSON results.

Now, switch to `main.js`. Select the search input and add an event
handler for `input` events. Also select the element on the page that
holds all of the search results; it's probably a `<ul>` element of
some kind.

Inside the event handler, you will first need to construct the
appropriate URL to make a request to. You can try to construct the
string directly, but it's a bit of a pain, because you need to handle
special characters like spaces the right way. Better to use [`URL`
objects](https://developer.mozilla.org/en-US/docs/Web/API/URL). Create
a new URL object for the `/api/s` URL, then use the [`searchParams`
field](https://developer.mozilla.org/en-US/docs/Web/API/URL/searchParams)
of that object to set the `q` parameter to the user's input.

Now `fetch` the URL; that returns a `Promise` so you'll need to
`await` the results. Once you have the result, call its `json` method
to decode the JSON response; that also returns a `Promise` so you'll
need to `await` that too.

Now might be a good time to pause and make sure things work. Add a
`console.log` call to log the JSON response, and try typing into the
search form. You should see your console print a new response every
time you type. If you see errors, fix them or get help.

Now that we have the JSON response, all we need to do is construct new
"cards" for each recipe in the JSON response. You can do this using
`createElement`, `append`, and ultimately `replaceChildren`, just like
in Phase 3; it's a bit tedious but just follow the exact same
structure in `card.html` and make sure to `append` each element you
create to its parent.

Test the result. You should be able to type into the search form and
see search results appear as you type. Very cool!

One thing that's a little less cool, though, is concurrency. If you
type faster than the network request comes back---this might be hard
on your local network, but is easy over the public internet---you can
have the search results flash between different versions or even show
out-of-date results. Let's fix that.

The idea is simple. In your `search_api` controller, extend your JSON
response with a `query` key:

```
{
    "results": [ ... ],
    "query": "tag:holiday"
}
```

Now, in your event handler, after you `await` the JSON results, check
that the `query` in the JSON response matches the value of the search
input before doing anything else. If they don't match, exit the event
handler without changing the page in any way.

The idea here is that the code after the `await` runs later, after the
network request finishes, and not while handling the `input` event.
The user might have typed more in the mean time, and the current value
of the search input might be different. If they are different, the
results we received are out of date and we can ignore them.



Write a cover sheet
-------------------

Run your server and view each page on your website in your browser.
Read through the requirements of Phases 1--5 and ensure that all
requirements are met. Test the show password checkbox, make sure the
total time and ingredients update correctly, and test
search-as-you-type.

Once you are sure everything works correctly, copy-and-paste the
following text into a new empty text file called "HW6.md":

```
Homework 6 Cover Sheet
----------------------

In this assignment, I completed:

- [ ] Phase 1
- [ ] Phase 2
- [ ] Phase 3
- [ ] Phase 4
- [ ] Phase 5

I discussed this assignment with:

- ...
- ...
- ...

- [ ] I solemnly swear that I wrote every line of code submitted as part
  of this assignment.

The most interesting thing I learned in this assignment was ...

The hardest thing in this assignment was ...
```

In the first list, replace `[ ]` with `[x]` for each phase of the
assignment you completed.

In the second list, replace the `...`s with the name of your partner
as well as any other person (student, friend, family, online stranger)
that you discussed this assignment with.

In the oath below that, check the box. Recall that, while you may
discuss the assignment in broad strokes, you must write every line of
code submitted by you, as stated in the oath below this list. This
includes the use of AI tools such as ChatGPT.

In the last two paragraphs, replace the `...` with the most
interesting and the most difficult aspect of this assignment. Don't
just make them a single sentence; the instructors use your answers to
make these assignments more interesting and easier.

Once you are done, commit everything and push it to Github.

How you will use this
---------------------

This is a fairly rudimentary set of front-end interactions, but all of
these are common. "Show password" checkboxes are important for mobile
users, while live-updating form fields and search results are common
across the web. Our implementations have some sharp edges (for
example, the search form should update the history, and also cancel
requests that go out of date), but they're basically workable versions
of features you've probably seen many times.

In production JavaScript code, some of these interactions---like the
"show password" or search-as-you-type search page---might be provided
by libraries, and some really common interactions like drag-and-drop
reordering or table sorting have many libraries available. But
something like the ingredient list updater would be custom to our
recipe application, and would probably have to be developed from
scratch.

Grading Rubrik
--------------

This assignment is worth 100 points. The different phases are worth
different weights:

**Phase 1** is worth 5 points. It is graded on:

- You link to a `main.js` file
- The `main.js` file is loaded and runs without error
- You use the `type=module` parameter

**Phase 2** is worth 10 points. It is graded on:

- There is a "show password" checkbox on the login page
- The "show password" checkbox and label look OK
- Checking and un-checking the checkbox shows and hides the password text
- There are no exceptions in the console on the login or other pages

**Phase 3** is worth 30 points. It is graded on:

- The total time field on the edit page updates when the prep or cook
  time fields change
- The total time is computed correctly
- The ingredients list on the edit page updates when any ingredient
  field changes
- The ingredients list is computed correctly
- The sort order of ingredients is correct
- There are no exceptions in the console on the edit or other pages

**Phase 4** is worth 20 points. It is graded on:

- The search form both in the page header and on the search page work
- The search query is shown on the search page correctly
- Searching for keywords and multiple keywords works correctly
- Searching for `tag:` keywords, including by clicking tag links,
  works correctly
- Searching for `variation:` keywords, including by clicking the "N
  variations" text, works correctly

**Phase 5** is worth 30 points. It is graded on:

- The `/api/s` API exists and returns properly-formatted JSON
  responses
- JavaScript makes `fetch` requests to the correct URLs
- Search results update as the user types
- Search results use the correct "card" format
- Out of date JSON responses are correctly ignored

**Cover Sheet** is worth 5 points. It is graded on:

- Cover sheet is formatted correctly.
- All questions on the cover sheet have coherent answers.

Note that if your cover sheet does not list all people you discussed
the assignment with, or misrepresents others' work as your own, that
is academic misconduct and can result in severe sanctions beyond the 5
points the cover sheet is worth. In the most severe cases, the
sanction for academic misconduct is failing this course.
