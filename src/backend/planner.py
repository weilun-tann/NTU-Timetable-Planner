"""
MAIN TIMETABLING LOGIC / SEARCH ALGORITHMS TO GENERATE
TIMETABLE COMBINATIONS GO HERE
"""
from collections import deque
from typing import List, Tuple, Dict

from .entities import Course, Index
from .json_parser import JSONParser


class Planner:
    @staticmethod
    def generate_combis(course_indexes: List[str]) -> List[Dict[Course, Index]]:
        courses = JSONParser.get_courses(sorted(course_indexes))
        combis = []
        Planner.backtrack(deque(courses), dict(), combis)
        return combis

    @staticmethod
    def backtrack(courses: deque[Course], combi: Dict[Course, Index], combis: List[Dict[Course, Index]]) -> None:
        if not Planner.validate(combi):
            return
        if not courses:
            combis.append(combi)
            return

        course = courses.popleft()
        for index in course.indexes:
            combi[course] = index
            Planner.backtrack(courses, combi, combis)
            del combi[course]

    @staticmethod
    def validate(combi: Dict[Course, Index]):
        intervals = Planner.get_intervals([index for index in combi.values()])
        return Planner.is_overlapping(intervals)

    @staticmethod
    def get_intervals(combi: List[Index]) -> List[Tuple[int, int]]:
        return sorted([(int(lesson.t_start), int(lesson.t_end)) for index in combi for lesson in index.lessons])

    @staticmethod
    def is_overlapping(intervals: List[Tuple[int, int]]) -> bool:
        for i in range(1, len(intervals)):
            last_end, curr_start = intervals[i - 1][0], intervals[i][0]
            if last_end > curr_start:
                return False
        return True
