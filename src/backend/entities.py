"""
ADD YOUR ENTITY CLASSES HERE
"""
from typing import List

from .json_parser import JSONParser


class Timeslot:
    times = ["0830", "0930", "1030", "1130", "1230",
             "1330", "1430", "1530", "1630", "1730",
             "1830", "1930", "2030", "2130", "2230"]
    time_to_slot = {times[i]: i for i in range(len(times) - 1)}


class Day:
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


class LessonType:
    LEC = "LECTURE"
    TUT = "TUTORIAL"
    LAB = "LAB"


class Lesson:

    def __init__(self, index: str, ltype: LessonType, group: str,
                 day: str, t_full: str, t_start: str, t_end: str,
                 duration: float, location: int, flag: int, remarks: str):
        self.index = index
        self.ltype = ltype
        self.group = group
        self.day = day
        self.t_full = t_full
        self.t_start = t_start
        self.t_end = t_end
        self.duration = duration
        self.location = location
        self.flag = flag
        self.remarks = remarks


class Index:
    def __init__(self, index: str):
        self.index = index
        self.lessons = JSONParser.get_lessons(self)


class Course:
    def __init__(self, code: str, name: str, au: int, indexes: List[Index]):
        self.code = code
        self.name = name
        self.au = au
        self.indexes = indexes
