CS 3550 Syllabus, Fall 2025
===========================

**Instructor**: Pavel Panchekha, [pavpan@cs.utah.edu](mailto:pavpan@cs.utah.edu), office MEB 2174 \
**Assistants**: Khoa, Phoebe, Victoria, TBD \
**Lecture**: Tue/Thu 9:10–10:30 in WEB L104 \
**Midterm**: Thu 2 October during class in WEB L104 \
**Final**: Mon 9 December at 8:00am in WEB L104 \
**Github**: https://github.com/utah-cs3550-fa25/ \
**Office Hours**: Thu 12:00–13:00 in MEB 2174; TBD \
**Piazza**: TBD

# About the Course

The goal of this class is to teach you how to develop basic web
applications, which means that by the end you will:

- understand the basic front-end and back-end architecture of web applications
- understand how to write HTML and style it with CSS
- understand how to write back-ends using a model-view-controller framework
- understand how to deploy web applications to the cloud
- understand how to set up authentication, authorization, and user roles

We've chosen technologies (Linux, Python, Django, AWS) that are both
popular and transferable, so the skills you gain will apply generally.

This course is a basic introduction to web development. It is a
foundation that CS 3540, CS 4550, CS 4560, and CS 6450 then build
upon to further your understanding of web application development.

# Cost

In this course you will deploy a web application to the cloud. This
can incur charges. First, you may need to purchase of a domain of your
choice; this typically costs about $10. Additionally, while we intend
your cloud deployment to stay within AWS's free tier, misuse or
misconfiguration can incur charges. Follow our instructions
diligently. Contact the instructors if either will be a problem.

# Assessment

Your grade will use the [standard 90/80/70/60 scale][grade] and
consists of:

| Component | Number | Weight, total     |
|-----------|--------|-------------------|
| Homeworks | 7      | 35% (so 5% each)  |
| Quizzes   | 5      | 15% (so 3% each)  |
| Exams     | 2      | 50% (so 25% each) |

[grade]: https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States#Grade_conversion

Homework assignments are cumulative: by the end of the course, you'll
have written a small "full-stack" web application. Assignments are due
Friday at the end of the day and must be submitted over Github.
However, a two-day extension is automatically granted (without any
grading penalty). Assignments later than that won't be accepted; with
cumulative assignments it is imperative that you do not fall behind.

The midterm will be during class time on 2 October, just before fall
break, and will cover all material from the first half of the class.
The final will be on 9 December at 8am, and will be cumulative.
Quizzes will be at the start of classes on 28 Aug, 11 Sept, 16 Oct, 30
Oct, and 13 Nov. All take place in the normal classroom. Instructors
may curve quizzes and exams up (but not down) to reach a target class
average.

# Attendance

This is an in-person class. Your attendance is assumed. Classes will
not be recorded, neither in general nor due to absence. (Feel free to
arrange that on your own with friends.) If you must be absent during a
quiz day, you must reach out to the instructors ahead of time. If you
are late to a quiz no make-up time will be given.

Disruptive, belittling, or rude behavior will not be tolerated,
including online. Remember: everyone in this class is here to learn.
If you already know the material, take a different class.

# Studying

This class is concept- and vocab-heavy. The web is a complex platform!
You are expected to study these concepts and vocabulary weekly.
Without studying, there's a good chance you'll do poorly on quizzes
and exams.

To help you study, we publish a comprehensive [Study
Guide](study-guide.md). This lists every concept, skill, and
vocabulary word that you're expected to know. We promise that
everything that appears on a quiz or exam will come from the study
guide.

If you don't have an existing study habit, we recommend flash cards.
You can use an app like [Quizlet](https://quizlet.com/) or
[Brainscape](https://www.brainscape.com/), or you can just use
physical flash cards. In either case, write the concept or vocabulary
word ("form method", say) on one side and the definition ("`get` for
read-only, otherwise `post`") on the other side.

Now test yourself. Look at one side and say out loud what's on the
other side. Flip the card and check if you got it right. If you're
right, put the card aside. If you got it wrong, put it back in the
deck so you see it again. Repeat until you've gotten all the cards
right. You can practice either side of the deck: say the definition
given the vocab word, or say the vocab word given the definition.

Go quick. Studying shouldn't be a chore. A few minutes every day works
better than cramming. If you get a card wrong often, review it more;
if you never get it wrong, review it less.

# Getting Help

Getting help early is the best way to succeed in this course. There
are three ways to get help in this course:

You can ask questions on Piazza. This will typically get you the
fastest responses, especially since other students can help you out.
Naturally, don't post your homework solutions, but short snippets that
you're struggling with are fine.

You can ask questions after class. This is a good way to get answers
to quick questions about your grade or assignment.

You can go to office hours. You will have the TA's undivided attention
during office hours, so this is a great way to get debugging help or
ask larger conceptual questions.

Do not wait to get help. It's much easier to not fall behind than it
is to catch up!

# Schedule

The following is an aspirational course schedule. It may change as the
course progresses; the instructor will announce changes in class.

| Week starting | Topic                                |
|---------------|--------------------------------------|
| August 18     | HTML                                 |
| August 25     | CSS, Quiz 1, **Homework 1 due**      |
| September 1   | Layout                               |
| September 8   | Flex-box, Quiz 2, **Homework 2 due** |
| September 15  | Django                               |
| September 22  | Back-ends, **Homework 3 due**        |
| September 29  | Review and **Midterm**               |
| October 6     | *Fall break*                         |
| October 13    | Forms, Quiz 3                        |
| October 20    | Auth, **Homework 4 due**             |
| October 27    | Security, Quiz 4                     |
| November 3    | JavaScript, **Homework 5 due**       |
| November 10   | AJAX, Quiz 5                         |
| November 17   | Cloud, **Homework 6 due**            |
| November 24   | Scaling                              |
| December 1    | Review, **Homework 7 due**           |
| December 8    | **Final**                            |

# Policies

**Cheating**. CS 3550 will follow the School of Computing’s cheating
policy. Basically, it's OK to discuss the assignment or your approach
with other students at a high level, but it is not OK to share code or
look at another student's code, or similar code found online. Academic
dishonesty results in a failing grade for the course, and two
instances of academic dishonestly lead to expulsion from the major.

**AI**. You must not use AI tools (such as ChatGPT, Copilot, and so
on) for any code you submit for an assignment. In an introductory
class like this, they work so well you won't learn the concepts you'll
need in later classes or in your career. That said, you are free to
use AI tools for other purposes, like helping debug problems,
answering general questions about web technologies, or providing
examples of how to use an API.

**Rounding**. Grades that end in ".9" will be rounded up to the next
whole number.

**Changes**. The syllabus can be changed with reasonable in-class
notice by the instructor.

Please also familiarize yourself with [University policies][u-policy]
on the ADA, safety, sexual misconduct, Covid, undocumented students,
drop/withdrawal, student mental health, student support, and academic
misconduct, as well as the [Kahlert School of Computing's academic
policies][ksoc-policy] and the [College of Engineering policies][coe-policy].

[u-policy]: https://cte.utah.edu/instructor-education/syllabus/institutional-policies.php
[ksoc-policy]: https://handbook.cs.utah.edu/current/Academics/policies.php
[coe-policy]: https://www.coe.utah.edu/students/current/semester-guidelines/
