# coding=utf-8

from __future__ import annotations
from models.element_set import ElementSet


class Container:
    def __init__(self, element_set: ElementSet):
        self.__elements = {}
        self.__element_set = element_set

    def add_element(self, name: str, value=None):
        element = self.__element_set.get_element(name)
        if element is not None:
            if value is not None:
                element.set_value(value)
            self.__elements[name] = element

    def modify(self, container: Container):
        """
        combines self and "incoming" container according to the rules of element interaction
        """
        pass

    def add_random(self):
        new_element_name = self.__element_set.get_random()
        new_value = self.__element_set.get_random_value(new_element_name)
        self.add_element(new_element_name, new_value)

    @property
    def elements(self):
        return self.__elements
