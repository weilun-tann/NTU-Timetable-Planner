from typing import Dict, List

from backend.entities import Course, Index


class TimetableCombinationsCache:
    def __init__(self):
        self.cache = dict()

    def get(self, course_indexes: List[str]):
        # print("GET", self.cache)
        return self.cache.get(tuple(course_indexes))

    def set(self, course_indexes: List[str], combis: List[Dict[Course, Index]]):
        self.cache[tuple(course_indexes)] = combis
        # print("SET", self.cache)
