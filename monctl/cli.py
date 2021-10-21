import click
from pathlib import Path
from .api import API
from .workspace import Workspace

@click.group()
def cli():
    """The CLI tool to manage courses on Mon School.
    """
    pass

@cli.command()
@click.option("--course", "course_name", help="course to push")
def push(course_name=None):
    """Push the courses to Mon School.

    If no course is specified, all courses are pushed.
    """
    api = API()
    w = Workspace()
    if course_name:
        names = [course_name]
    else:
        names = w.list_courses()

    for name in names:
        course = w.read_course(name)
        api.update_course(course)

@cli.command()
@click.argument("filenames", type=click.Path(exists=True), nargs=-1, required=True)
def push_lesson(filenames):
    """Push on or more lessons to Mon School.
    """
    api = API()
    w = Workspace()
    for f in filenames:
        lesson = w.read_lesson(Path(f))
        api.update_lesson(lesson)

def main():
    cli()