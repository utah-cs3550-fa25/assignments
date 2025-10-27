CS 3550 Assignment 5 (Permissions)
==================================

**Status**: Phase 1 Final, Phase 2--5 draft \
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

Open your `settings.html` file. Add the following line somewhere in
the file:

    LOGIN_URL = "/login"

In your `views.py` file, add the following line to the top:

    from django.contrib.auth import authenticate, login, logout

Next, open up the `login.html` template. It should contain an HTML
form; make sure this form makes a `POST` request to `/login` and
contains the mandatory `{% csrf_token %}` tag. As usual, this form
submits to its own URL. Also make sure that each `<input>` inside that
form has a `name` and an appropriate `type`.

Find your `login_form` controller. Modify it so that, for `POST`
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
controller. Modify the `header.html` template to add a "Log out" link,
next to the "View Profile" link, that takes the user to `/logout`.

Test that logging out works correctly. When you are logged out, you
should see "AnonymousUser" as the username in the header.

Test that you can log in, see your user's name in the header, then log
out, and see AnonymousUser in the header. If the auto-tester passes,
you are done with this phase.

[docs-auth]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.authenticate
[docs-login]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.login
[docs-logout]: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.logout
