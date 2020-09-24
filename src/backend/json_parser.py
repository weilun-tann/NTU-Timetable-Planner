"""
EVERYTHING YOU NEED FROM THE RAW JSON FILE, ADD IT AS A
METHOD HERE TO GIVE YOU THE PROCESSED VERSION
"""

import json
from typing import List, Dict

from entities import Course, Lesson, Index


class JSONParser:

    @staticmethod
    def get_dict():
        with open('data/2020_S1.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def get_courses(data: Dict, course_codes: List[str]) -> List[Course]:
        courses = []
        for code in course_codes:
            course = data[code]
            name = course["name"]
            au = course["au"]
            indexes = JSONParser.get_indexes(data, code)
            courses.append(Course(code, name, au, indexes))
        return courses

    @staticmethod
    def get_indexes(data: Dict, course_code: str) -> List[Index]:
        indexes = []
        for index in data[course_code]["index"]:
            lessons = JSONParser.get_lessons(data, course_code, index["index_number"])
            indexes.append(Index(index, lessons))
        return indexes

    @staticmethod
    def get_lessons(data: Dict, course_code: str, index: str) -> List[Lesson]:
        lessons = []
        for ind in data[course_code]["index"]:
            if ind["index_number"] == index:
                for det in ind["details"]:
                    lessons.append(Lesson(index, det["type"], det["group"],
                                          det["day"], det["time"]["full"],
                                          det["time"]["start"], det["time"]["end"],
                                          det["time"]["duration"], det["location"],
                                          det["flag"], det["remarks"]))
        return lessons

    @staticmethod
    def get_lectures(data: Dict, index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_tutorials(data: Dict, index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_labs(data: Dict, index: Index) -> List[Lesson]:
        pass
