"""
ADD YOUR ENTITY CLASSES HERE
"""
from django.core.serializers.json import DjangoJSONEncoder
from typing import List


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
                 duration: float, location: int, flag: int, remarks: str, date: str):
        self.index = index
        self.ltype = ltype
        self.group = group
        self.day = day
        self.t_full = t_full
        self.t_start = t_start[0:2] + ':' + t_start[2:4] + ':00'
        self.t_end = t_end[0:2] + ':' + t_end[2:4] + ':00'
        self.duration = duration
        self.location = location
        self.flag = flag
        self.remarks = remarks
        self.date = date

    def __json__(self):
        return dict(index=self.index, ltype=self.ltype, group=self.group, day=self.day,
                    t_full=self.t_full, t_start=self.t_start, t_end=self.t_end,
                    duration=self.duration, location=self.location, flag=self.flag,
                    remarks=self.remarks, date=self.date)


class Index:
    def __init__(self, index: str, lessons: List[Lesson]):
        self.index = index
        self.lessons = lessons

    def __json__(self):
        return dict(index=self.index, lessons=self.lessons)


class Course:
    def __init__(self, code: str, name: str, au: int, indexes: List[Index]):
        self.code = code
        self.name = name
        self.au = au
        self.indexes = indexes

    def __json__(self):
        return dict(code=self.code, name=self.name, au=self.au, indexes=self.indexes)


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        else:
            print(obj.__json__())
            raise ValueError(f"{obj} is NON-SERIALIZABLE")
