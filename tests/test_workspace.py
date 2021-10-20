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
  - name: datatypes
    title: Datatypes
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
