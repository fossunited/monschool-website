from monctl import workspace
import yaml

COURSE_YML = """
name: python-primer
title: Python Primer
suffix: pp
short_introduction: Introduction to Python
description: Practical introduction to Python
instructor: foobar
is_published: 0
chapters:
  - name: introduction
    title: Introduction
    lessons:
      - introduction/getting-started.md
      - introduction/hello-world.md
  - name: datatypes
    title: Datatypes
"""

LESSON_TEXT = """\
---
title: Getting Started
include_in_preview: 0
---

Getting Started with Python
"""

class TestWorkspace:
    def test_read_course(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        w = workspace.Workspace(str(tmp_path))
        assert w.read_course("python-primer") == {
            "name": "python-primer",
            "title": "Python Primer",
            "suffix": "pp",
            "short_introduction": "Introduction to Python",
            "description": "Practical introduction to Python",
            "instructor": "foobar",
            "is_published": 0,
            "chapters": ["introduction-pp", "datatypes-pp"]
        }

    def test_read_chapter(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        w = workspace.Workspace(str(tmp_path))
        assert w.read_chapter("python-primer", "introduction") == {
            "name": "introduction-pp",
            "title": "Introduction",
            "lessons": ["getting-started-pp", "hello-world-pp"]
        }

    def test_read_lesson(self, tmp_path):
        path = tmp_path / "python-primer" / "course.yml"
        path.parent.mkdir()
        path.write_text(COURSE_YML)

        path2 = path.parent.joinpath("introduction", "getting-started.md")
        path2.parent.mkdir()
        path2.write_text(LESSON_TEXT)

        w = workspace.Workspace(str(tmp_path))
        assert w.read_lesson(path2) == {
            "name": "getting-started-pp",
            "chapter": "introduction-pp",
            "title": "Getting Started",
            "include_in_preview": 0,
            "body": "Getting Started with Python"
        }
