---
title: Generating Files for All Lessons
include_in_preview: false
---

Once you've created a `course.yml` with all the lesson files listed, you can use a command to generate the stub files all the lessons.

```
$ python manage.py generate --course rust-for-beginners
generated courses/rust-for-beginners/introduction/welcome.md
generated courses/rust-for-beginners/introduction/rustup.md
generated courses/rust-for-beginners/introduction/first-rust-program.md
generated courses/rust-for-beginners/introduction/why-rust.md
generated courses/rust-for-beginners/control-flow/conditionals.md
generated courses/rust-for-beginners/control-flow/iteration.md
...
```

You can replace `rust-for-beginners` with the name of the course that you are creating and it will create stub files for every lesson.

If a file is already present, it won't overwrite it. So, you can use it whenever you add a new lesson to the course.

The top-section of the file includes the title of the lesson. You can edit the title if required. More information about the format of the lesson is explained in the next section.

Once you generate the files for all the lessons, you can send your first pull request. Make sure you include the `course.yml` file and one file for each lesson in the pull request.
