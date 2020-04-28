# coding=utf-8

from collections import namedtuple
from models.scale import Scale
from random import randint


class Element:
    def __init__(self, name: str, category: str, scale: Scale):
        self.__name = name
        self.__category = category
        self.__scale = scale

    def __repr__(self):
        return f"{self.__class__.__qualname__} {self.name} {self.category} {self.current_value}"

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def scale(self):
        return self.__scale

    def modify(self, value):
        self.__scale.modify(value)

    def set_value(self, value):
        self.__scale.set_value(value)

    def get_random_value(self):
        return randint(self.__scale.min_value, self.__scale.max_value)