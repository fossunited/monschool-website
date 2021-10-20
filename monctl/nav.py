"""
monctl.nav
~~~~~~~~~~

Hooks for injecting navigation to mkdocs.
"""
import yaml
from pathlib import Path

class Course:
    def __init__(self, root, name):
        self.root = root / "courses" / name
        self.name = name
        self.data = self.read_course_yaml()

    def read_course_yaml(self):
        path = self.root / "course.yml"
        return yaml.safe_load(path.open())

    def make_nav(self):
        title = self.data['title']
        nav_chapters = [self.make_chapter_nav(chapter) for chapter in self.data['chapters']]
        return {title: nav_chapters}

    def make_chapter_nav(self, chapter):
        title = chapter['title']
        nav_lessons = [self.make_lesson_nav(lesson) for lesson in chapter['lessons']]
        return {title: nav_lessons}

    def make_lesson_nav(self, lesson):
        return f"{self.name}/{lesson}"

def list_courses():
    root = Path(".")
    for p in root.joinpath("courses").iterdir():
        if p.is_dir() and p.joinpath("course.yml").exists():
            yield Course(root, p.name)

def on_files(files, config):
    """This is called by mkdocs and is used to dynamically generate navigation for the website.
    """
    courses = list_courses()
    config['nav'] = [course.make_nav() for course in courses]
