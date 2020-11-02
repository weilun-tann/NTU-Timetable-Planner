"""
MAIN TIMETABLING LOGIC / SEARCH ALGORITHMS TO GENERATE
TIMETABLE COMBINATIONS GO HERE
"""
from collections import deque
from typing import Dict, Deque, List, Set, Tuple

from backend.entities import Course, Index
from backend.json_parser import JSONParser


class Planner:
    @staticmethod
    def generate_combis(course_indexes: List[str], free_days: List[str]) -> List[Dict[Course, Index]]:
        courses = JSONParser.get_courses(sorted(course_indexes))
        combis = []
        Planner.backtrack(len(courses), deque(courses), dict(), combis, free_days)
        return combis

    @staticmethod
    def backtrack(num_courses: int, courses: Deque[Course], combi: Dict[Course, Index],
                  combis: List[Dict[Course, Index]], free_days: List[str]) -> bool:

        if not Planner.valid(combi, free_days):
            return False
        if not courses:
            if len(combi) == num_courses:
                combis.append(combi.copy())
            return True

        course = courses.popleft()
        res = False

        for index in course.indexes:
            combi[course] = index
            res = Planner.backtrack(num_courses, courses, combi, combis, free_days)
            if not res: del combi[course]
        if not res:
            courses.appendleft(course)
        return res

    @staticmethod
    def valid(combi: Dict[Course, Index], free_days: List[str]) -> bool:
        intervals = Planner.get_intervals([index for index in combi.values()])
        return not Planner.clashes(intervals, free_days)

    @staticmethod
    def get_intervals(combi: List[Index]) -> List[Tuple[str, str, str]]:
        return [(lesson.day, str(lesson.t_start), str(lesson.t_end)) for index in combi for lesson in index.lessons]

    @staticmethod
    def clashes(intervals: List[Tuple[str, str, str]], free_days: List[str]) -> bool:
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):

            # CHECK IF WE CHOSE A FREE DAY
            if intervals[i - 1][0] in free_days or intervals[i][0] in free_days:
                print('VIOLATION OF FREE DAYS!')
                return True

            # CHECK IF THERE IS A CLASH IN TIMINGS
            if intervals[i - 1][0] == intervals[i][0]:
                last_end, curr_start = intervals[i - 1][2], intervals[i][1]
                if last_end > curr_start:
                    return True
        return False

    @staticmethod
    def get_alt_indexes(clicked_index: str, combi: Dict[str, str]) -> List[Index]:
        course_codes = [k for k, v in combi.items() if v == clicked_index]
        if not course_codes: return []
        course_code = course_codes[0]
        combi = {k: [i for i in JSONParser.get_indexes(k) if i.index == v][0] for k, v in combi.items() if
                 v != clicked_index}
        indexes = JSONParser.get_indexes(course_code)
        filtered_indexes = [i for i in indexes if
                            Planner.valid({**combi, **{course_code: i}}) and i.index != clicked_index]
        return Planner.deconflict(filtered_indexes)

    @staticmethod
    def deconflict(filtered_indexes: List[Index]) -> List[Index]:
        booked_timings = set()
        deconflicted_indexes = []
        for idx in filtered_indexes:
            conflict = False
            for lesson in idx.lessons:
                timing = (lesson.day, lesson.t_start, lesson.t_end)
                if timing in booked_timings:
                    conflict = True
                    break
            if not conflict:
                booked_timings.add(timing)
                deconflicted_indexes.append(idx)
        return deconflicted_indexes

    @staticmethod
    def serialise(combinations):
        serialise = []
        i = 0
        for combination in combinations:
            serialise.append({})
            for course in combination:
                serialise[i][course.name] = []
                j = 0
                for index in course.indexes:
                    serialise[i][course.name].append({index.index: []})
                    for lessons in index.lessons:
                        serialise[i][course.name][j][index.index].append(
                            {"date": lessons.date, "t_start": lessons.t_start, "t_end": lessons.t_end,
                             "ltype": lessons.ltype})
                    j += 1
            i += 1
        return serialise

    @staticmethod
    def get_free_days(params: Dict) -> List[str]:
        days = ["MON", "TUE", "WED", "THU", "FRI"]
        return [d for d in days if params.get(d)]


if __name__ == "__main__":
    Planner.generate_combis(["CZ2001", "CZ2002", "CZ2003", "CZ2004", "CZ2005", "CZ2006"])
