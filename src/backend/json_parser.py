"""
EVERYTHING YOU NEED FROM THE RAW JSON FILE, ADD IT AS A
METHOD HERE TO GIVE YOU THE PROCESSED VERSION
"""

import json
from datetime import timedelta, datetime
from typing import List, Dict

from backend.entities import Course, Lesson, Index


class JSONParser:

    @staticmethod
    def get_dict():
        with open('../backend/data/2020_S1.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def get_courses(course_codes: List[str]) -> List[Course]:
        courses = []
        for code in course_codes:
            course = DATA[code]
            name = course["name"]
            au = course["au"]
            indexes = JSONParser.get_indexes(code)
            courses.append(Course(code, name, au, indexes))
        return courses

    @staticmethod
    def get_indexes(course_code: str) -> List[Index]:
        indexes = []
        for index in DATA[course_code]["index"]:
            lessons = JSONParser.get_lessons(course_code, index["index_number"])
            indexes.append(Index(index["index_number"], lessons))
        return indexes

    @staticmethod
    def get_lessons(course_code: str, index: str) -> List[Lesson]:
        lessons = []
        for ind in DATA[course_code]["index"]:
            if ind["index_number"] == index:
                for det in ind["details"]:
                    lessons.append(Lesson(index, det["type"], det["group"],
                                          det["day"], det["time"]["full"],
                                          det["time"]["start"], det["time"]["end"],
                                          det["time"]["duration"], det["location"],
                                          det["flag"], det["remarks"], JSONParser.get_date(det),
                                          course_code))
        return lessons

    @staticmethod
    def get_course_names() -> List[str]:
        return {k: v['name'] for k, v in DATA.items()}

    @staticmethod
    def get_full_course_names(course_codes: List[str]) -> List[str]:
        course_names = JSONParser.get_course_names()
        return [f"{code} {course_names.get(code)}" for code in course_codes]

    @staticmethod
    def get_date(details: Dict) -> str:
        curr_day = datetime.today().weekday()  # 0 - MON, 6 - SUN
        curr_date = datetime.today()
        day_date = JSONParser.get_day_date_map(curr_day, curr_date)
        return day_date[details["day"]]

    @staticmethod
    def get_day_date_map(curr_day: int, curr_date: datetime) -> Dict[str, str]:
        day_date = dict()
        day_map = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}

        # BACK-FILL
        for i in range(curr_day + 1):
            day_date[day_map[curr_day - i]] = JSONParser.datetime_to_ymd(curr_date + timedelta(days=-i))

        # FORWARD-FILL
        for i in range(7 - curr_day):
            day_date[day_map[curr_day + i]] = JSONParser.datetime_to_ymd(curr_date + timedelta(days=i))

        return day_date

    @staticmethod
    def datetime_to_ymd(dt: datetime) -> str:
        return dt.strftime('%Y-%m-%d')


DATA = JSONParser.get_dict()
