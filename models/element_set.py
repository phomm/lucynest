# coding=utf-8

from models.scale import Scale
from models.element import Element
from random import choice, randint


class ElementSet:
    def __init__(self):
        self.__elements = {}
        self.__fill()

    def __fill(self):
        # colors
        self.__add_color('red', 100)
        self.__add_color('blue', 100)
        self.__add_color('green', 100)
        self.__add_color('yellow', 100)
        self.__add_color('orange', 100)
        self.__add_color('purple', 100)
        self.__add_color('brown', 100)
        self.__add_color('skyblue', 100)
        self.__add_color('black', 100)
        self.__add_color('white', 100)
        # motorics
        self.__add_motoric('run', 100)
        self.__add_motoric('offend', 100)
        self.__add_motoric('fall', 100)
        self.__add_motoric('headrush', 100)
        self.__add_motoric('rhythmo', 100)
        self.__add_motoric('laugh', 100)
        self.__add_motoric('wound', 100)
        self.__add_motoric('touch', 100)
        self.__add_motoric('tickles', 100)
        # feelings
        self.__add_feeling('fear', 100)
        self.__add_feeling('pain', 100)
        self.__add_feeling('joy', 100)
        self.__add_feeling('sadness', 100)
        self.__add_feeling('sweet', 100)
        self.__add_feeling('sour', 100)
        self.__add_feeling('bitter', 100)
        self.__add_feeling('charm', 100)
        self.__add_feeling('trust', 100)
        self.__add_feeling('hot', 100)
        self.__add_feeling('cold', 100)

    def __add(self, name: str, category: str, value):
        scale = Scale(0, value, value / 2)
        element = Element(name, category, scale)
        self.__elements[name] = element

    def __add_color(self, name: str, value):
        self.__add(name, "color", value)

    def __add_motoric(self, name: str, value):
        self.__add(name, "motoric", value)

    def __add_feeling(self, name: str, value):
        self.__add(name, "feeling", value)

    def get_element(self, name: str) -> Element:
        if name in self.__elements.keys():
            return self.__elements[name]
        return None

    @property
    def count(self):
        return len(self.__elements)

    @property
    def elements(self):
        return self.__elements.values()

    def get_random(self):
        return choice(list(self.__elements.keys()))

    def get_random_value(self, element_name):
        element = self.get_element(element_name)
        if element is None:
            return None
        return element.get_random_value()
