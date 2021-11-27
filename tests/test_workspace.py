from build import workspace
import yaml

COURSE_YML = """
name: python-primer
title: Python Primer
suffix: pp
short_introduction: Introduction to Python
description: Practical introduction to Python
instructor: foobar
draft: false,
is_published: true
upcoming: true
preview_image: null
tags:
  - python
  - beginner
video_link:
chapters:
  - name: introduction
    title: Introduction
    description: Introduction to Python
    lessons:
      - introduction/getting-started.md
      - introduction/hello-world.md
  - name: datatypes
    title: Datatypes
    description: Exploring Datatypes in Python
    lessons: []
"""

LESSON_TEXT = """\
---
title: Getting Started
include_in_preview: false
---

Getting Started with Python
"""

class TestWorkspace:
    def test_read_course(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        w = workspace.Workspace(str(tmp_path))
        c = w.read_course("python-primer")
        assert c.dict() == yaml.safe_load(path.open())

        assert c.get_doc() == {
            "name": "python-primer",
            "title": "Python Primer",
            "short_introduction": "Introduction to Python",
            "description": "Practical introduction to Python",
            "instructor": "foobar",
            "is_published": 1,
            "upcoming": 1,
            "tags": "python,beginner",
            "video_link": None,
            "chapters": [{"chapter": "introduction-pp"}, {"chapter": "datatypes-pp"}]
        }

    def test_chapter_doc(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        w = workspace.Workspace(str(tmp_path))
        c = w.read_course("python-primer")
        chapter = c.get_chapter("introduction")
        assert chapter.get_doc() == {
            "course": "python-primer",
            "name": "introduction-pp",
            "title": "Introduction",
            "description": "Introduction to Python",
            "lessons": [{"lesson": "getting-started-pp"}, {"lesson": "hello-world-pp"}]
        }

    def test_read_lesson(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        path2 = path.parent.joinpath("introduction", "getting-started.md")
        path2.parent.mkdir()
        path2.write_text(LESSON_TEXT)

        w = workspace.Workspace(str(tmp_path))
        lesson = w.read_lesson(path2)

        assert lesson.dict() == {
            "name": "getting-started",
            "title": "Getting Started",
            "include_in_preview": False,
            "body": "Getting Started with Python"
        }
        assert lesson.chapter.name == 'introduction'

        assert lesson.get_doc() == {
            "chapter": "introduction-pp",
            "name": "getting-started-pp",
            "title": "Getting Started",
            "include_in_preview": False,
            "body": "Getting Started with Python"
        }
