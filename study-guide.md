Study Guide
===========

This document lists vocabulary, concepts, and syntax that you're
expected to know for the midterm and final. You should use this
document to study outside of class.

HTML
----

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

CSS
---

**Basic CSS**: You should be able to write CSS code that uses tag, ID,
and class selectors, plus the `:hover` pseudo-class, and compound
selectors using the space combination type. You should be able to
write selectors to select various elements on an HTML page.

You should know the following CSS properties:

- `font-family`, `font-weight`, `font-style`, `font-size`, and
  `text-decoration`
- `color`, `background-color`, and `opacity`
- `border` (the three-value form) and its subproperties like
  `border-bottom` or `border-left-width`
- `border-radius` (the one-value form)

You should be able to explain the cascading rule, inheritance, and
shorthand properties.

**Legacy layout**: You should be able to identify where the padding,
margin, and border areas of a box are. You should be able to define
inline and block layout mode. You should be able to write a
`max-width` or `min-width` media query.

You should be able to use the following types of values:

- For lengths, the `px`, `rem`, `vw`, and `vh` units
- For colors, hex colors or named colors
- For `line-height`, numeric multipliers
- The CSS named fonts `serif`, `sans-serif`, `monospace`

**Flex-box**: You should be able to create complex layouts using
flex-box layout, including nested layouts with rows and columns. This
involves knowing how to use the the `display: flex` and
`flex-direction` properties, the `width`/`height`, `flex-grow`, and
`flex-shrink` properties, and the `justify-content`, `gap`, and
`align-items` properties.

Knowing the properties and their values is not enough! You should be
able to design complex layouts using flex-box, starting from
screenshots or wireframes. The [Notes](notes.md#flex-box) have a short
checklist you can follow to build complex flex-box layouts. You should
feel comfortable using this checklist to create layouts from
screenshots or wireframes. It is important to practice this.

Django and MVC
--------------

You should be able to define clients, servers, the client-server
architecture, requests, and responses.

You should be able to explain the roles of the model, view, and
controller, and router in a MVC-style web application. You should be
able to explain the roles of standard Django project files like
`settings.py`, `urls.py`, `models.py`, `views.py`, the `migrations/`
folder, the `static/` folder, and the `templates/` folder.

**Models**: You should know the following Django field types:

- `IntegerField`, `FloatField`, and `DecimalField`
- `CharField` and `TextField`
- `DateField` and `DateTimeField`
- `FileField` and `ImageField`

You should be able to identify which field is appropriate in various
situations, and also be able to use the `max_length`, `blank`, `null`,
and `default` attributes.

You should be able to model complex relationships in web application
state using `ForeignKey` relationships, including choosing `on_delete`
behavior.

**Views**: You should know how to use the `render` function in
controllers.

You should know the following Django template filters:

- `default`
- `floatformat`, `date`, `timesince`
- `join`, `length`, `pluralize`

You should know the `for`, `if`, `with`, and `include` Django template
tags and the `forloop.first`, `forloop.last`, `forloop.counter`, and
`forloop.counter0` variables.

**Controllers**: You should know the syntax for defining URLs,
including parameterized URLs, in `urls.py`.

You should be able to query, create, and save Django model objects.
Specifically, you should know the following query operators:

- `filter`, `exclude`, `union`, `intersection`, and `distinct`
- `order_by` and `reverse`
- `count` and `aggregate`
- `first` and `last`
- `contains` and `exists`

You should be able to use to query objects by field (as in
`author="Tom Clancy"`; by field of a related object (as in
`author_name="Tom Clancy"`); or by property of a field (as in
`author_name__contains="Tom"`).

You should be able to explain the "1 + N" problem and be able to use
`select_related` to fix it.

You should be able to explain migrations, when they are created, when
they are run, and what problem they solve.

----------------------------------------------------

Topics below this line are not on the midterm, even if they were
covered in class before the midterm was assessed.

----------------------------------------------------

Forms
-----

**Forms** You should know how to make a valid HTML form, including the
`<form>`, `<label>`, `<input>`, `<button>`, and `<output>` elements.
You should know what the `action`, `method`, and `enctype` parameters
do on forms, and be able explain the difference between the `get` and
`post` values for `method` and choose the right one for various forms.
(You are not expected to know what values to put for `enctype`, but
you are expected to know in what case you need to set a non-default
`enctype`.) You should know the `type`, `id`, `name`, `value`, and
`disabled` attributes on input elements.

For `<input>` elements, you should know the `checkbox`, `radio`,
`file`, `image`, `date`, `time`, `text`, `number`, `email`, and `tel`
types.

You should be able to write a Django view function (controller) that
receives form data and saves it to the database. You should know how
to use the `request.GET`, `request.POST`, and `request.FILES`
dictionaries to access form data. You should be able to describe the
risks associated with file uploads.

**Validation**: You should know how to catch `DoesNotExist` errors
from queries and return `Http404` errors. You should know how to
catch `ValueError`s from parsing numbers. You should be able to write
a form handler that re-renders on failure and redirects on success,
and where the re-rendering uses some errors data structures.

You should be able to use the following input element attributes for
client-side validation:

- `required`
- `min` / `max`
- `minlength` / `maxlength`
- `accept`

You should also be able to use `:valid` / `:invalid` to style HTML
forms.

Security
========

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
==========

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
=================

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

