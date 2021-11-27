---
title: Adding Content to Lessons
include_in_preview: false
---

Now that you are the course outline and stubs for each of the lessons, it is the time to see how to add content to each lesson. The content of each lesson is formatted using Markdown.

## The Lesson Format

The contents of each lesson file would be in the following format.

```
---
title: Functions Closures
include_in_preview: false
---

contents of the lesson.
```

The first part is called the _frontmatter_ and it include the title of the lesson and whether not this lesson is included in course preview. It is suggested to leave that to `false` when you are creating the course.

The second part is the body of the lesson in markdown.

While, you can use all the markdown features, it is recommended to follow the following guidelines to make the course look consistent.

* Use second-level heading (`##`) for section headings in the lesson
* Make sure you enclose variable names and other inline code snippets in backticks.

    For example:

    <table>
    <tr>
    <td>
    ```
    The function `circle` draws a circle on the screen.
    ```
    </td>
    <td>
    The function `circle` draws a circle on the screen.
    </td>
    </tr>
    </table>

The system supports including examples and exercises in lessons. We'll how to do that in the next lessons.
