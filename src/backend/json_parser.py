"""
EVERYTHING YOU NEED FROM THE RAW JSON FILE, ADD IT AS A
METHOD HERE TO GIVE YOU THE PROCESSED VERSION
"""

from typing import List

from .entities import Course, Lesson, Index, Timeslot


class JSONParser:

    @staticmethod
    def get_courses(course_indexes: List[str]) -> List[Course]:
        pass

    @staticmethod
    def get_indexes(course_code: str) -> List[Index]:
        pass

    @staticmethod
    def get_lessons(index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_lectures(index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_tutorials(index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_labs(index: Index) -> List[Lesson]:
        pass

    @staticmethod
    def get_timeslot(lesson: Lesson) -> Timeslot:
        pass
