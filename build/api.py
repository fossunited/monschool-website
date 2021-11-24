"""
monctl.api
~~~~~~~~~~

Client library to push courses to mon.school.
"""
import os
from pathlib import Path

import frontmatter
from frappeclient import FrappeClient
import yaml

from .workspace import Lesson, Chapter, Course

def _read_config_value(name, default=None):
    value = os.getenv(name) or default
    if value is None:
        raise Exception(f"Please provide {name} environment variable")
    return value

def get_config():
    return {
        "site_url": _read_config_value("MON_SCHOOL_URL", "https://mon.school/"),
        "api_key": _read_config_value("MON_SCHOOL_API_KEY"),
        "api_secret": _read_config_value("MON_SCHOOL_API_SECRET")
    }

DEFAULTS = {
    "LMS Course": {
        "title": "-",
        "short_introduction": "-",
        "description": "-"
    },
    "Course Chapter": {
        "title": "-",
        "description": "-"
    },
    "Course Lesson": {
        "title": "-",
        "body": "-"
    }
}

class API:
    def __init__(self):
        self.config = get_config()
        self.frappe = self.get_frappe()

    def get_frappe(self):
        url = self.config['site_url'].rstrip("/")
        api_key = self.config['api_key']
        api_secret = self.config['api_secret']

        frappe = FrappeClient(url)
        frappe.authenticate(api_key, api_secret)
        return frappe

    def save_document(self, doctype, name, doc):
        #print("save_document", doctype, name, doc)
        data = {
            "doctype": doctype,
            "name": name,
            "doc": doc
        }
        old_doc = self.get_doc(doctype, name)
        old_doc = old_doc and self.subdict(old_doc, doc.keys()) or {}
        old_doc = self.trim_tables(old_doc)

        if old_doc == doc:
            print(doctype, name, "no changes found")
        else:
            print(doctype, name, "saving...")
            return self.invoke_method("mon_school.api.save_document", data=data)

    def trim_tables(self, doc):
        def trim(d):
            ignore = "name owner creation modified modified_by parent parentfield parenttype idx docstatus doctype".split()
            return {k: v for k, v in d.items() if k not in ignore}

        for key, value in doc.items():
            if isinstance(value, list):
                doc[key] = [trim(v) for v in value]
        return doc

    def subdict(self, d, keys):
        return {k: d[k] for k in keys if k in d}

    def get_doc(self, doctype, name):
        return self.frappe.get_doc(doctype, name)

    def exists(self, doctype, name):
        return bool(self.get_doc(doctype, name))

    def invoke_method(self, method, data):
        url = self.frappe.url + "/api/method/" + method
        result = self.frappe.session.post(url, json=data).json()
        if "message" not in result:
            print("ERROR:", result)
            raise Exception(f"Failed to invoke method: {method}")

        message = result['message']
        if message.get("ok"):
            return message
        else:
            raise Exception(message.get("error") or f"unknown error: {message}")

    def update_course(self, course: Course):
        self.ensure_doc("LMS Course", course.name)
        for chapter in course.chapters:
            self.ensure_doc("Course Chapter", chapter.docname, course=course.name)

        doc = course.get_doc()
        doc['instructor'] = self.resolve_username(doc["instructor"])
        self.save_document("LMS Course", course.name, doc)

        for chapter in course.chapters:
            self.update_chapter(chapter)

    def update_chapter(self, chapter: Chapter):
        doc = chapter.get_doc()
        self.ensure_doc("Course Chapter", doc['name'], course=doc['course'])
        for lesson in doc["lessons"]:
            name = lesson["lesson"]
            self.ensure_doc("Course Lesson", name=name, title=name, chapter=doc["name"])

        self.save_document("Course Chapter", doc['name'], doc)

        for lesson in chapter.get_lessons():
            self.update_lesson(lesson)

    def resolve_username(self, username):
        rows = self.frappe.get_list("User", fields=['name'], filters={"username": username})
        if not rows:
            return "Administrator"
        else:
            return rows[0]["name"]

    def update_lesson(self, lesson: Lesson):
        course_name = lesson.chapter.course.name
        chapter_name = lesson.chapter.docname
        doc = lesson.get_doc()

        self.ensure_doc("LMS Course", course_name)
        self.ensure_doc("Course Chapter", chapter_name, course=course_name)
        self.save_document("Course Lesson", doc['name'], doc)

    def ensure_doc(self, doctype, name, **fields):
        if not self.exists(doctype, name):
            doc = dict(DEFAULTS[doctype], **fields)
            self.save_document(doctype, name, doc)
