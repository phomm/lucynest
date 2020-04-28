# coding=utf-8

from collections import namedtuple
# from math import


class Scale:
    def __init__(self, min_value, max_value, current_value):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__current_value = current_value

    def set_value(self, value):
        self.__current_value = self.__clamp(value)

    def modify(self, value):
        self.set_value(self.__current_value + value)

    def __clamp(self, candidate):
        return max(min(candidate, self.__max_value), self.__min_value)

    @property
    def min_value(self):
        return self.__min_value

    @property
    def max_value(self):
        return self.__max_value

    @property
    def current_value(self):
        return self.__current_value


