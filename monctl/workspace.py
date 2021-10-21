"""
monctl.workspace
~~~~~~~~~~~~~~~~

Module to read the courses, chapters, lessons from the disk.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List
from pathlib import Path
import frontmatter
import yaml

class Workspace:
    def __init__(self, root="courses"):
        self.root = Path(root)
        self.cache = {}

    def read_yaml_file(self, path: Path):
        if path not in self.cache:
            self.cache[path] = yaml.safe_load(path.open())
        data = self.cache[path]
        return dict(data)

    def list_courses(self):
        return [p.name for p in self.root.iterdir() if p.joinpath("course.yml").exists()]

    def read_course(self, name: str) -> Course:
        path = self.root.joinpath(name, "course.yml")
        data = self.read_yaml_file(path)

        course = Course(
            root=path.parent,
            name=name,
            suffix=data['suffix'],
            title=data['title'],
            short_introduction=data['short_introduction'],
            description=data['description'],
            instructor=data['instructor'],
            is_published=data['is_published'],
            chapters=[])

        course.chapters = [self.parse_chapter(course, c) for c in data['chapters']]
        return course

    def parse_chapter(self, course: Course, data: dict) -> Chapter:
        name = data['name'] + "-" + course.suffix
        return Chapter(
            name=data['name'],
            course=course,
            title=data['title'],
            description=data['description'],
            lessons=[Path(p) for p in data['lessons']]
        )

    def read_lesson(self, path: Path):
        chapter_name = path.parent.name
        course_name = path.parent.parent.name
        course = self.read_course(course_name)
        chapter = course.get_chapter(chapter_name)
        return chapter.get_lesson(path.stem)

@dataclass
class Course:
    """Course as represented in the workspace.
    """
    root: Path
    name: str
    suffix: str
    title: str
    short_introduction: str
    description: str
    instructor: str
    is_published: bool
    chapters: List[Chapter]

    def get_doc(self) -> dict:
        doc = CourseDoc(
            name=self.name,
            title=self.title,
            short_introduction=self.short_introduction,
            description=self.description,
            instructor=self.instructor,
            is_published=int(self.is_published),
            chapters=[{"chapter": c.docname} for c in self.chapters]
        )
        return asdict(doc)

    def get_chapter(self, name):
        chapters = {c.name: c for c in self.chapters}
        return chapters[name]

    def dict(self):
        d = dict(self.__dict__)
        del d['root']
        d['chapters'] = [c.dict() for c in self.chapters]
        return d

@dataclass
class CourseDoc:
    """Course as represented in mon.school
    """
    name: name
    title: str
    short_introduction: str
    description: str
    instructor: str
    is_published: int
    chapters: List[str]

@dataclass
class Chapter:
    name: str
    title: str
    description: str
    course: Course
    lessons: List[Path]

    @property
    def docname(self):
        return self.name + "-" + self.course.suffix

    def get_lessons(self):
        return [Lesson.from_file(chapter=self, path=self.course.root.joinpath(str(p))) for p in self.lessons]

    def get_lesson(self, name):
        paths = {p.stem: p for p in self.lessons}
        path = self.course.root / str(paths[name])
        return Lesson.from_file(chapter=self, path=path)

    def get_doc(self) -> dict:
        doc = ChapterDoc(
            course=self.course.name,
            name=self.docname,
            title=self.title,
            description=self.description,
            lessons=[{"lesson": p.stem + "-" + self.course.suffix} for p in self.lessons]
        )
        return asdict(doc)

    def dict(self):
        return {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "lessons": [str(p) for p in self.lessons]
        }

@dataclass
class ChapterDoc:
    course: str
    name: str
    title: str
    description: str
    lessons: List[str]

@dataclass
class Lesson:
    chapter: Chapter
    path: Path
    name: str
    title: str
    body: str
    include_in_preview: bool


    @property
    def docname(self):
        return self.name + "-" + self.chapter.course.suffix

    @staticmethod
    def from_file(chapter: Chapter, path: Path):
        text = path.read_text()
        data = frontmatter.loads(text)

        return Lesson(
            chapter=chapter,
            path=path,
            name=path.stem,
            title=data['title'],
            body=data.content.strip(),
            include_in_preview=data.get('include_in_preview') or False
        )

    def get_doc(self):
        doc = LessonDoc(
            chapter=self.chapter.docname,
            name=self.docname,
            title=self.title,
            body=self.body,
            include_in_preview=int(self.include_in_preview))
        return asdict(doc)

    def dict(self):
        return {
            "name": self.name,
            "title": self.title,
            "body": self.body,
            "include_in_preview": self.include_in_preview
        }

@dataclass
class LessonDoc:
    chapter: str
    name: str
    title: str
    body: str
    include_in_preview: bool
