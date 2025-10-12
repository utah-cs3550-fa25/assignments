Study Guide
===========

This document lists vocabulary, concepts, and syntax that you're
expected to know for the midterm and final. You should use this
document to study outside of class.

HTML and CSS
------------

**Basic HTML**: You should be able read HTML and associate HTML code
with the parts of the web page it renders. You should be able to
explain the meaning of these tags and their arguments:

- Write valid HTML using the doctype, `<meta>`, `<link>`, `<title>`
- Style text using `<a>`, `<em>`, `<strong>`, `<code>`, `<img>`
- Structuring text using `<p>`, `<h1>` through `<h6>`
- Structure pages using `<nav>`, `<header>`, `<footer>`, `<main>`
- Tabulate data with `<table>`, `<tr>`, and `<td>`
- Write lists using `<ul>`, `<ol>`, `<li>`
- Special syntax like comments `<!-- -->` and escapes `&lt;`

You should be able to identify and fix incorrect HTML syntax,
including mis-nested or un-closed tags, invalid attribute syntax or
missing attributes, mis-nesting block and inline content, and mis-use
of look-alike tags such as `<head>`, `<header>`, and `<h1>` or `<a>`
and `<link>`.

**Accessibility**: You should know key accessibility requirements,
such as proper heading hierarchies, textual alternatives for images,
and language attributes, and be able to detect when these are absent.
You should know the `lang` and `alt` attributes and the `<label>`
element. You should know the landmark elements: `<main>`, `<nav>`,
`<header>`, and `<footer>`.

**Selectors**: You should be able to use type, class, and ID
selectors. You should be able to use descendant (a.k.a. "space")
selectors and the `:hover` selector. Given an HTML page you should be
able to write selectors for various elements on that page.

**Properties**: You should know the following CSS properties and how
to write values for them:

- `font-family`, `font-weight`, `font-style`, `font-size`, and
  `text-decoration`
- `text-align`
- `color`, and `background-color`
- `border` and `border-bottom`, specifically the three-valued form
- `border-radius`
- `display` specifically when set to `none`

You should be able to explain the cascading rule, inheritance, and
shorthand properties. For colors, you should be able to write named
and hex colors. For fonts, you should know the named `serif`,
`sans-serif`, and `monospace` fonts.

Layout
------

**Flex-box**: You should know how to create a row or column using
`display: flex` and the `flex-direction` property, and be able to
identify flex containers and flex items. You should be able to use
`width` and `height` to change the size of flex items, use `gap` to
add gaps between them, and use `padding` between the flex container
and flex items. You should be able to use `px` and `rem` units.

You should understand the main and cross axes of a flex container. You
should be able to distribute white-space with the `justify-content`
and `align-items` properties, know which is which, and the common
values for each. You should know the `flex-grow` and `flex-shrink`
properties, and how to use them. You should be able to limit growing
and shrinking with `min`/`max` properties for `width` and `height`,
and how to set `flex-wrap`.

You should be able to explain default layout properties and what a CSS
reset does. (You don't need to memorize the reset syntax itself.)

**Nested flex-box**: You should be able to design complex layouts by
nesting multiple flex rows and columns, starting from screenshots or
wire-frames. We recommend the following set of steps:

- Draw a wireframe that marks each element and identifies rows and
  columns. You may need to modify the wireframe as you go, if you
  determine that you need extra wrapper elements.
- Then, start at the outer-most flex container and work inward.
- First determine the main axis lengths of each flex item. Is it sized
  to content or is it a specific size?
- Then determine how main axis whitespace is distributed. Is there a
  minimum gap? Is there padding? Where does extra whitespace go?
- Finally determine how cross axis whitespace is distributed. Do
  elements stretch?

Practice creating complex layouts using this check-list; this is often
the most difficult skill for students.

**Responsive layout**: You should be able to write `@media` rules
using `max-width` or `min-width` predicates. You should be able to
write `calc` values, like for grids. You should be able to write
responsive layouts that change from row to column or hide elements at
various screen sizes.

Django and MVC
--------------

You should be able to define clients, servers, the client-server
architecture, requests, and responses, and give examples. You should
be able to define the roles of the back-end and the front-end.

You should be able to explain the roles of the model, view,
controller, and router in a MVC-style web application. You should also
know the Django names for each, which, annoyingly, differ. You should
be able to explain the roles of standard Django project files like
`settings.py`, `urls.py`, `models.py`, `views.py`, the `migrations/`
folder, the `static/` folder, and the `templates/` folder.

**Models**: You should know basic Django field types like
`IntegerField`, `FloatField`, `TextField`, and `FileField`. You should
be able to determine whether `CharField` or `TextField` is more
appropriate. You should be able to use the `max_length`, `blank`,
`null`, and `default` attributes.

You should understand what a `ForeignKey`, a `ManyToManyField`, and a
`OneToOneField` are. You should understand when to set `related_name`
and `symmetrical`. You should be able to choose appropriate
`on_delete` behaviors. You should be able to model complex
relationships using these fields and properties.

You should be able to explain migrations, when they are created, when
they are run, and what problem they solve.

**Controllers**: You should know the syntax for defining URLs,
including parameterized URLs, in `urls.py`. You should be able to use
`get` or `get_object_or_404` to retrieve objects from the database,
and `save` to create and modify them.

You should be able to query model objects using `filter`, `exclude`,
and `order_by`. You should be able to use to query objects by field
(as in `author="Tom Clancy"`; by field of a related object (as in
`author__name="Tom Clancy"`); or by property of a field (as in
`author__name__contains="Tom"`). You should be able to traverse
relations in both directions.

You should know when queries are executed, including for related
objects. You should be able to explain and fix the "1 + N" problem
using `select_related` or `prefetch_related`. You should be able to do
`Min`, `Max`, `Count`, and `Sum` queries with `aggregate`.

**Views**: You should be able to write simple controllers that take
arguments, perform queries, construct data structures, and call
`render`. You should know the `for`, `if`, `include` Django template
tags and the `default` filter. You should know how to add model
methods.

----------------------------------------------------------------------

Topics below this line are not on the midterm, even if they were
covered in class before the midterm was assessed. Items below this
line may be changed before fall break.

----------------------------------------------------------------------

Forms
-----

**Forms** You should know how to make a form using the `<form>`,
`<label>`, `<input>`, `<button>`, and `<output>` elements. You should
know what the `action`, `method`, and `enctype` parameters do, and
choose between `get` and `post`. (You are not expected to know what
values to put for `enctype`, but you are expected to know in what case
you need to set a non-default `enctype`.) You should know the `type`,
`id`, `name`, `value`, and `disabled` attributes on input elements.

You should know the `checkbox`, `radio`, `file`, `image`, `date`,
`time`, `text`, `number`, `email`, and `tel` types of `<input>`.

You should be able to write a Django view function (controller) that
receives form data and saves it to the database. You should know how
to use the `request.GET`, `request.POST`, and `request.FILES`
dictionaries to access form data. You should be able to describe the
risks associated with file uploads.

**Validation**: You should know how to catch `DoesNotExist` and
`ValueError`s. You should be able to write a form handler that
re-renders on failure and redirects on success, and where the
re-rendering uses shows errors saved in some data structure.

You should be able to explain the difference between client-side and
server-side validation, and explain the security concerns with each.
You should be able to use the `required`, `min`/`max`,
`minlength`/`maxlength`, and `accept` attributes for client-side
validation, and style invalid elements with `:valid`/`:invalid`.

Security
--------

You should be able to describe simple security policies in terms
of which users can perform which actions. You should be able to
explain cookies, identity, and session data. You should be able to
describe, at a high level, how user logins work via sessions and
cookie. You should be able to define authorization and authentication. 

You should be able to use `request.user`, `authenticate`, `login`, and
`logout` for logging users in and out. You should be able to test if a
Django `User` is a member of a `Group` and raise `PermissionDenied` if
an authorization check fails. You should be able to explain the benefits
of centralized access control checks.

You should be able to explain what an injection vulnerability is, and
what the benefits and risks are of using `|safe` or `.raw()` in
Django. You should be able to explain what CSRF is, what `{%
csrf_token %}` outputs, and what the risks are of using
`@csrf_exempt`. You should be able to explain what an open redirect
is, and what to look for in your code to find it. You should be able
to explain what a CVE is and who/what OWASP is.

JavaScript
----------

You should be able to include JavaScript into an HTML page. You should
know the syntax of a `<script>` tag, how to write inline JS, and what
the `defer` parameter does. You should also know what `type=module`
does, at least at a high level (allows `import`, separate namespace).
You should be able to explain the idea of progressive enhancement.

You should be comfortable with basic JavaScript syntax. You should
also know what to avoid: type mixing, accidental globals, `var`
declarations, `for` loops with undeclared or `var`-declared variables,
`for`/`in` loops, `function` inline functions, and the `this`
variable. You should know `Arrays.from` and the difference between
arrays and array-like objects.

You should be able to use jQuery's `$` for wrapping, selecting, and
creating elements. You should have an idea what APIs require unwrapped
elements (like `e.target`) and which expect jQuery APIs and how to
wrap (`$`) and unwrap (`Array.from`). You should be able to use the
following jQuery APIs for manipulating elements:

- `append`, `prepend`, `before`, `after`, `remove`, `replace`
- `addClass`, `removeClass`, `val`, `attr`
- `children`, `parent`, `find`, `next`, `previous`
- `text`
- `data`

You should be able to attach event handlers with jQuery's `on` method
and know the `target` field and `preventDefault` method on events.

You should know about the `$.ajax` function, including at least the
`method` and `data` fields in the options object. You should be able
to make asynchronous requests using the `success` callback. You should
be able to handle errors using the `error` callback. You should be
able to use `$.ajax` as a promise with `await`. You should be know how
to move `await` calls later in the code to enable more parallelism.

Cloud Deployments
-----------------

You should be able to identify the parts of a URL: the protocol (or
scheme), hostname (or domain), port, and path (or page). You should be
able to explain the relationship between hostnames (also called
domains), IP addresses, and packet routes, and be able to distinguish
between them.

You should be able to explain the role of a registrar. You should know
what A and AAAA records do in DNS. You should be able to give the
price, within an order of magnitude, of a domain ($5-20/yr), an IPv4
address ($30-50), an IPv6 address ($0), inbound bandwidth ($0),
outbound traffic ($50-100/TB), and an HTTPS certificate ($0). You
should be able to explain why you need an IPv4 address.

You should be able to explain the roles of AWS and its EC2 and Elastic
IP services. You should be give the cost, within an order of
magnitude, of the deployment you were asked to create as part of
Assignment 7 (about $9/mo). You should be able to explain the terms
"instance" and "instance type". You should be able to explain what
burstable CPUs are in AWS.

You should be able describe briefly what Linux, SystemD, APT, SSH, and
JournalCtl do. You should be able to explain the role of the gateway
server and the database server. You should be able to explain what the
`DEBUG` and `ALLOWED_HOSTS` settings in Django do and why they differ
between development and deployment.

You should be able to define RPS and give RPS estimates for smaller
(10-30 for a `t3.medium`) and larger instances (100-200 for a
`c5.large`). You should be able to explain AMIs and auto-scaling.

