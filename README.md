# Mon School

This repository maintains all the courses published on [Mon School][].

[Mon School]: (https://mon.school/).

NOTE: This repository is no longer used to submit changes to mon.school. Please use the web interface on https://mon.school/ make updates to the courses.

## Setup

To make it easier to author courses, [Material for MkDocs][mkdocs] is used to serve the website as HTML. Even though there will be differences the layout of this and the final website, this is a convenient interface to author courses for [Mon School][].

[mkdocs]: https://squidfunk.github.io/mkdocs-material/

## Dev Instance

To setup a dev instance:

Step 1: Clone the Repository

```
$ git clone https://github.com/fossunited/monschool-website
```

Step 2: Install dependencies

```
$ pip install -r requirements.txt
```

You can also do this in a virtualenv.

Step 3: Run dev server to serve the courses

```
$ make
...
INFO     -  [08:58:56] Serving on http://127.0.0.1:8000/
```

Open <https://localhost:8000/> to see the courses. Pick the course on the nav bar to see the contents of the course.

Make changes to lesson files and see them reflected in the site live.

# Docs

Coming soon!
