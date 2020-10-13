"""
MAIN TIMETABLING LOGIC / SEARCH ALGORITHMS TO GENERATE
TIMETABLE COMBINATIONS GO HERE
"""
from collections import deque
from typing import List, Tuple, Dict, Deque

from backend.entities import Course, Index
from backend.json_parser import JSONParser


class Planner:
    @staticmethod
    def generate_combis(course_indexes: List[str]) -> List[Dict[Course, Index]]:
        data = JSONParser.get_dict()
        courses = JSONParser.get_courses(data, sorted(course_indexes))
        combis = []
        Planner.backtrack(len(courses), deque(courses), dict(), combis)

        print("\nSOLUTION")
        for combi in combis:
            print(f"Solution {combis.index(combi)}")
            for c, i in sorted(combi.items(), key=lambda c: c[0].code):
                print(f"{c.code}, {i.index['index_number']}")
            print()

        print(f"Combinations found : {len(combis)}")
        return combis

    @staticmethod
    def backtrack(num_courses: int, courses: Deque[Course], combi: Dict[Course, Index],
                  combis: List[Dict[Course, Index]]) -> bool:

        if not Planner.valid(combi):
            return False
        if not courses:
            if len(combi) == num_courses:
                combis.append(combi.copy())
            return True

        course = courses.popleft()
        res = False

        for index in course.indexes:
            # pprint(f"Index : {vars(index)}")
            combi[course] = index
            res = Planner.backtrack(num_courses, courses, combi, combis)
            if not res: del combi[course]
        if not res:
            courses.appendleft(course)
        return res

    @staticmethod
    def valid(combi: Dict[Course, Index]) -> bool:
        intervals = Planner.get_intervals([index for index in combi.values()])
        return not Planner.clashes(intervals)

    @staticmethod
    def get_intervals(combi: List[Index]) -> List[Tuple[str, int, int]]:
        return sorted(
            [(lesson.day, str(lesson.t_start), str(lesson.t_end)) for index in combi for lesson in index.lessons])

    @staticmethod
    def clashes(intervals: List[Tuple[str, int, int]]) -> bool:
        for i in range(1, len(intervals)):
            # CHECK IF SAME DAY FIRST
            if intervals[i - 1][0] == intervals[i][0]:
                last_end, curr_start = intervals[i - 1][2], intervals[i][1]
                if last_end > curr_start:
                    return True
        return False


if __name__ == "__main__":
    Planner.generate_combis(["CZ2001", "CZ2002", "CZ2003", "CZ2004", "CZ2005", "CZ2006"])
