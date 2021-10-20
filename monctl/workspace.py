"""
monctl.workspace
~~~~~~~~~~~~~~~~

Module to read the courses, chapters, lessons from the disk.
"""
from pathlib import Path
import yaml

class Workspace:
    def __init__(self, root="courses"):
        self.root = Path(root)
        self.cache = {}

    def read_yaml_file(self, path: Path):
        if path not in self.cache:
            d = yaml.safe_load(path.open())
            self.cache[path] = d
        data = self.cache[path]
        print(data)
        return dict(data)

    def read_course(self, name):
        path = self.root.joinpath(name, "course.yml")
        course = self.read_yaml_file(path)
        name_suffix = course['suffix']
        course['chapters'] = [c['name'] + "-" + name_suffix for c in course['chapters']]
        return course

