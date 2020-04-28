# coding=utf-8

from __future__ import annotations
from models.container import Container
from models.element_set import ElementSet
from models.container import Container
from random import randint


class Actor:

    def _fill(self):
        for _ in range(randint(1, 5)):
            self._container.add_random()

    def __init__(self, name: str, element_set: ElementSet):
        self._element_set = element_set
        self._name = name
        self._container = Container(element_set)
        self._fill()

    @property
    def name(self):
        return self._name

    @property
    def elements(self):
        return self._container.elements.values()


