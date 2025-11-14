CS 3550 Assignment 5 (Permissions)
==================================

**Status**: Final \
**Due**: Phase 1 due **31 Oct**, Phase 2--5 due **7 Nov**

About
-----

In this assignment you'll add user authentication and authorization to
your application. Specifically, you will:

- Set up a login system for users
- Require login for actions like editing recipes
- Enforce public and private recipes
- Set up file uploads and secure them

The assignment is due Friday, 7 Nov before midnight. The course's
normal extension policy applies.

Phase 1: Enabling logins
------------------------

Open your `settings.py` file. Add the following line somewhere in the
file:

    LOGIN_URL = "/login"

In your `views.py` file, add the following line to the top:

    from django.contrib.auth import authenticate, login, logout

Next, open up the `login.html` template. It should contain an HTML
form; make sure this form makes a `POST` request to `/login` and
contains the mandatory `{% csrf_token %}` tag. As usual, this form
submits to its own URL. Also make sure that each `<input>` inside that
form has a `name` and an appropriate `type`.

Find your `singup` controller. Modify it so that, for `POST`
requests, it:

1. Extracts the username and password from the POST request;
2. Then calls [Django's `authenticate` function][docs-auth]
   (this function either returns a `User` object or `None`);
3. If authentication succeeds,
   calls [Django's `login` function][docs-login]
   and then redirects to the `/profile/USERNAME` page.
4. If authentication fails, re-renders the form,
   same as if it were a `GET` request.

You can access the current user in templates via the `user` variable;
you don't need to explicitly pass it in. In the `header.html`
template, display the user's `get_full_name`. This step is important
because it allows you to test whether or not you actually logged in.

Test that you can log in and see the user you've logged in as on the
profile page. If you've run `makedata.py`, you can log in as:

- The admin user `pavpan`
- The normal users `a`, `b`, `c`, and `d`

Each user's password is the same as their username.

Next, define a `signout` controller. This controller should call
[Django's `logout` function][docs-logout] and redirect to `/login`.
Modify `urls.py` so that `/logout` routes to this new `signout`
controller. Modify the `header.html` template to add a "Sign out"
link, next to the "View Profile" link, that takes the user to
`/logout`.

Test that logging out works correctly. When you are logged out, you
should see "AnonymousUser" as the username in the header.

Test that you can log in, see your user's name in the header, then log
out, and see AnonymousUser in the header. If the auto-tester passes,
you are done with this phase.

[docs-auth]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.authenticate
[docs-login]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.login
[docs-logout]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.logout



Phase 2: A nicer login form
---------------------------

We can make the login process a little smoother. For starters, in
`header.html`, modify the template to not show the username and
profile link when not logged in; instead, just show a simple "Sign in"
link to the login page.

Also, after you log in, you should be redirected back to whatever page
you were originally on. To do so, include a `next` parameter in the
login link whose value is `request.get_full_path`.

Then, inside the `signin` controller, read that `next` parameter out
of `request.GET`. Pass that to the `login.html` template. (If there's
no `next` variable, use `/` as the default.)

In the `login.html` template, add a `hidden` input element named
`next`. Read that `POST` parameter in the `POST` branch of `signin`.
Redirect to that parameter when login is successful. If the login
fails, pass that same `next` parameter when re-rendering the login
form, so it still works when the user submits the form again.

Note the chain of events here---the user is first sent to the login
page, and in this first `GET` request there's a `next` parameter. Then
they fill out the form, making a *second* request, which contains a
`next` parameter too but as a `POST` parameter. We plumb this `next`
parameter from the first request to the second. Then when handling the
second request we use that to do the redirect.

Test that you can log out, go to some specific page, like `/recipe/7`,
click the "Sign in" link, sign in, and end up back on `/recipe/7` but
now logged in.

However, as implemented, this is an "open redirect", a classic
application security vulnerability. For example, if you visit

    http://localhost:8000/login?next=https%3A%2F%2Fgoogle.com

and log in, you'll find yourself redirected to `google.com`, a site
you don't control. Not good!

Let's patch this vulnerability. Before redirecting to the `next`
parameter, check that this `next` URL 1) begins with a `/`, and 2)
does not begin with `//`. Both checks must pass before you redirect.
If one of the checks fails, you still redirect, but to `/` instead of
whatever was in the `next` URL.



Phase 3: Public and private recipes
-----------------------------------

Now that we have user login set up, we need to restrict which users
can do which actions.

Logged-out users shouldn't be able to edit recipes. We can enforce
that with the `login_required` decorator. Add the following line to
your `views.py`:

    from django.contrib.auth.decorators import login_required

You can now use the [`login_required` decorator][docs-logreq] to mark
certain views as being inaccessible when not logged in. Make the
`edit_recipe` view `login_required`.

[docs-logreq]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#the-login-required-decorator

Make sure you can view an edit page, like `/recipe/7/edit`, when
logged in, but not when logged out.

Moreover, even a logged-in user should only be able to edit their own
recipe. Modify `recipe.html` so that it *does not show* the "Edit" button
unless the current user is the recipe author. You can do this entirely
in the template.

On its own, not showing the button is a purely client-side protection.
We always need server-side protection too. So, at the top of
`edit_recipe`, check that the current user is the recipe author. If
not, throw a `PermissionDenied` exception (you'll need to import it).

Add an `is_public` boolean field to your `Recipe` model; default it to
False; make a migration. Update your local checkout of the
`assignments` repository. Delete and recreate your database following
the instructions in [Assignment 3](hw3.md); the `makedata.py` script
should automatically detect the `is_public` field and use it, making
some recipes public and some private for each user.

Modify the `profile` and `search` controllers to exclude non-public
recipes, but to _include_ the current user's non-public recipes. There
are a few ways to do this using the [`union` method][dq-union] or [`Q`
objects][dq-q]. Make sure you don't show the current user's public
recipes twice. Test your logic by logging in as a specific user (say,
`a`), noting what recipes you see on the user's profile page (say,
`/profile/a`), and then logging out and viewing the same page again.
You should see private recipes when logged in but not when logged out.

[dq-union]: https://docs.djangoproject.com/en/5.2/ref/models/querysets/#union
[dq-q]: https://docs.djangoproject.com/en/5.2/ref/models/querysets/#q-objects

Modify the `recipe` controller to raise `PermissionDenied` when the
recipe is not public and the current user is not the recipe author. If
you think about it, excluding these recipes from search results is a
client-side protection and requires a server-side analog. Banning
access is that server-side protection.

In your `recipe.html` page, you should already have a small `GET` form
that contains an "Edit" button. If the recipe is private, add another
form that submits to `/recipe/ID/makepublic`. The form should be a
`POST` form and have a "Make Public" button. Route that URL to a new
`make_public` controller. That controller should only respond to
`POST` requests, require logins, and raise `PermissionDenied` if the
current user isn't the recipe author. If they _are_ the author, it
should set `is_public` to `True` and redirect back to the recipe page.
Don't forget to save the `Recipe`! In this case we only have a
server-side protection but no analogous client-side protection because
if a recipe is private, no one but the author should see the recipe
page at all.

Check that:

- The author of a private recipe can edit it or make it public
- The author of a public recipe can edit it
- A non-author cannot view or edit or make public a private recipe
- A non-author can view, but not edit, a public recipe



Phase 4: Images and image uploads
---------------------------------

Until now, recipe images haven't been showing up. Let's fix that.

Create a `recipe_image` controller and route `/recipe/ID/photo` to it.
Inside that controller, load the recipe object, check that it has a
`photo` (if it doesn't, return 404), and then return:

    FileResponse(recipe.photo.open("rb"), "image/png")

The argument to `open` here tells Python that we want to **r**ead the
file in **b**inary mode (because images are binary, not text). You'll
need to import `FileResponse`.

In `recipe.html` and `card.html`, make sure your `img` elements point
to `/recipe/ID/photo` as the image source, and only include the `img`
if the recipe actually has a photo. You should see photos show up for
a few of the recipes.

Make a similar `profile_image` controller for `/profile/USER/photo`,
and make profile pages show user profiles. Ben Braiser's page
(`/profile/b`) should now have a profile photo.

Next, edit `edit.html`. Make sure its `img` element points to the same
place. Below it, add a new `<input>` element of `file` type. Name it
something unique and give it a label like "Recipe photo". You should
now see a button for uploading a recipe photo when editing a recipe.

Add an `enctype` to the form so that it can handle file uploads.

In the `edit_recipe` controller, load the uploaded image from
`request.FILES` and save it as the recipe photo, but only if the name
is actually present in `request.FILES`. If there's no upload, we don't
want to delete the existing photo, just leave it alone. Make sure that
after uploading a photo, you can see it on the recipe page.

The photos of private recipes should be private. Modify `recipe_image`
to raise `PermissionDenied` if the recipe is private and the current
user isn't the recipe author. Test it by logging in as some user,
finding a private recipe, uploading a photo for it, confirming that it
shows up on the recipe page, and then visiting `/recipe/ID/photo`. You
should see just the photo. Now log out, visit that same
`/recipe/ID/photo` URL, and make sure you now cannot view the photo.
Make sure public recipe photos are still visible.



Phase 5: Securing image uploads
-------------------------------

We also want to make sure file uploads do not harm our server.

First, check your `models.py` file and make sure your image fields
`upload_to` the `media/` folder. This is important because it means
we'll never confuse a user upload (which lives in `media/`) with any
other file (which always lives elsewhere, that is, we'll never store
something of our own in `media/`).

Let's also limit uploaded files to 64MiB. In your `edit_recipe`
controller, when a recipe image is included, check its the `size`
field. If it is too large (that is, over 64 MiB), add an error message
complaining about this. Adding the error message should also block the
`save` call so avoid saving the uploaded file to our server. It's
important that we use the `size` field instead of trying to read the
file: if an evil user uploaded a really big file, reading that file
might use a lot of memory or disk space. So we must check the file
size before we access the file's contents.

Let's further limit uploads to PNG files. *After* checking the `size`
of the uploaded image, check that its `name` field ends with `.png`.
That's nice, but not secure; computers don't actually determine what
kind of file something is by looking at the file extension. Instead,
they look at the first few bytes of the file and check them against a
[big database of "magic bytes"][magic-bytes]. The magic bytes for PNG
are `89 50 4E 47`; note that these are hex values, not decimal.

[magic-bytes]: https://en.wikipedia.org/wiki/List_of_file_signatures

We want to do this check too. First, read the first "chunk" of the
uploaded file with `next(file.chunks())`. Reading the first chunk,
instead of the whole file, is much faster. Then, check the first four
bytes of this chunk against the PNG magic bytes. You can access the
bytes of chunk with `chunk[0]`, `chunk[1]`, and so on, and you can
write hex constants in Python using `0x89`, `0x50`, and so on.
If the magic bytes don't match (or if the file doesn't end with
`.png`), again show an error message instead of saving the file.

Test that you can't upload some other type of file (like a PDF) file,
even if you first rename it to `.png`. Also test that you can't upload
a very big file. Once you've tested that, set the file upload input
element's `accept` attribute to `image/png`; now, when you click the
button, it should make it easy for you to upload PNG images
specifically.

Finally, not only do we not want uploaded files to harm our
server---we also don't want them to harm other users. Move the size
and PNG checks to an `is_small_png` function, and call it in your
`recipe_photo` and `profile_photo` helpers. The reason we're doing
these tests twice (once on upload and once when viewing) is so that,
if we ever add more checks, they'll apply retroactively to
already-uploaded files. Raise an `Http404` error if any of these tests
fail.

You can test this code by 1) disabling the PNG checks and the `accept`
parameter in the edit page / controller; 2) uploading a non-PNG file;
3) making sure you still can't view the invalid PNG file. Make sure to
turn the checks back on so you get credit for them.

> [!WARNING]
> This is not a complete list of steps you'd need to take to make
> image uploads safe (for example---is it really safe for users to
> view arbitrary, untrusted PNG files?). Nor is security the only
> troublesome part of handling uploads (what if users try to
> distribute illegal images via your website?). Support for file
> uploads and especially downloads opens you up to a lot of possible
> attacks, some of them difficult to prevent. But it's a good start!



Write a cover sheet
-------------------

Read through the requirements of Phases 1--5 and ensure that all
requirements are met. Try viewing pages you don't have permissions to,
or making POST requests you're not supposed to make. Try abusing the
open redirect, or uploading invalid or very large files. If you find
any problems, use the browser developer tools or `print` debugging to
understand and correct the problem.

Once you are sure everything works correctly, copy-and-paste the
following text into a new empty text file called "HW5.md" in the root
of your repository:

```
Homework 5 Cover Sheet
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

Once you are done, commit everything and push it to Github. **Make
sure to include the text "Please grade" in your final commit message**
to help TAs identify the right commit to grade.

How you will use this
---------------------

Almost any large web application has a notion of identities,
authentication, and authorization. The specific implementation here is
simple but is sufficient for most small and even medium-sized
applications. More complex authorization and authentication schemes,
as necessary in applications with plugins or for integration between
different systems, are still grounded in core ideas like identity and
permission.

Separately, file uploads almost always come with extensive security
checks, similar or even more stringent than the ones used here. Images
are a pretty simple case! Videos and documents (like DOCX, XLSX, PDF)
are harder. You should be quite careful about allowing users to upload
arbitrary files to your server. It may not be worth the security issues!

Grading Rubrik
--------------

This assignment is worth 100 points. The different phases are worth
different weights:

**Phase 1** is worth 5 points. It is graded on:

- The login form must log users in using a `POST` request
- The login form must reject invalid users and passwords
- After a successful login, the user should be redirected
- The logout endpoint should log users out
- The site header should show the current user and a sign out link
  when logged in
  
If you pass all auto-tests, then you have completed this phase.

**Phase 2** is worth 15 points. It is graded on:

- The site header should show a sign in link
- Signing in via the sign in link should redirect you back to the page
  you were originally on
- The open redirect prevention must be done correctly

**Phase 3** is worth 40 points. It is graded on:

- Only the recipe author should be able to edit a recipe or even view
  the edit form
- The edit button should not be shown unless the user is the recipe
  author
- Recipes should have an `is_public` field, with some public and some
  private recipes
- All pages should only show public recipes, plus the current user's
  private recipes.
- Viewing another user's private recipes should not be possible
- When viewing one's own private recipes, there should be a "Make
  Public"  button, and clicking it should make the recipe public
- Only the recipe author should be able to make a recipe public

**Phase 4** is worth 20 points. It is graded on:

- The `/recipe/ID/photo` URL should show a recipe photo (if there is
  one)
- Recipe photos should show up both on the recipe page and on the
  "cards" pages.
- The profile photo for Ben Braiser should also show up. Only Ben
  should have a profile photo.
- Photo uploads should work
- Not selecting a photo when submitting the edit form should leave the
  current photo in place
- Photos of private recipes should only be visible to the recipe
  author

**Phase 5** is worth 15 points. It is graded on:

- Uploads are saved to the `media/` folder
- Only files 64 MiB or smaller can be uploaded
- Only PNG files can be uploaded (checked with file name and initial bytes)
- Only PNG files can be viewed, even if uploaded

**Cover Sheet** is worth 5 points. It is graded on:

- Cover sheet is formatted correctly.
- All questions on the cover sheet have coherent answers.

Note that if your cover sheet does not list all people you discussed
the assignment with, or misrepresents others' work as your own, that
is academic misconduct and can result in severe sanctions beyond the 5
points the cover sheet is worth. In the most severe cases, the
sanction for academic misconduct is failing this course.
