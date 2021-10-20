"""
monctl.workspace
~~~~~~~~~~~~~~~~

Module to read the courses, chapters, lessons from the disk.
"""
from pathlib import Path
import frontmatter
import yaml

FIELDS = {
    "LMS Course": "title instructor is_published short_introduction description chapters"
}

class Workspace:
    def __init__(self, root="courses"):
        self.root = Path(root)
        self.cache = {}

    def read_yaml_file(self, path: Path):
        if path not in self.cache:
            self.cache[path] = yaml.safe_load(path.open())
        data = self.cache[path]
        return dict(data)

    def read_course(self, name):
        path = self.root.joinpath(name, "course.yml")
        course = self.read_yaml_file(path)
        name_suffix = course['suffix']
        course['chapters'] = [c['name'] + "-" + name_suffix for c in course['chapters']]
        return course

    def read_chapter(self, course_name, name):
        path = self.root.joinpath(course_name, "course.yml")
        course = self.read_yaml_file(path)
        name_suffix = course['suffix']
        for c in course['chapters']:
            if c['name'] == name:
                doc = dict(c)
                doc['name'] = doc['name'] + "-" + name_suffix
                doc['lessons'] = [Path(p).stem + "-" + name_suffix for p in doc['lessons']]
                return doc

    def read_lesson(self, path: Path):
        course_yml = path.parent.parent.joinpath("course.yml")
        # print("course_yml")
        course = self.read_yaml_file(course_yml)
        name_suffix = course['suffix']

        text = path.read_text()
        data = frontmatter.loads(text)

        doc = dict(data)
        doc['name'] = path.stem + "-" + name_suffix
        doc['body'] = data.content.strip()
        doc['chapter'] = path.parent.stem + "-" + name_suffix
        return doc
