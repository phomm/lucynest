# coding=utf-8

from __future__ import annotations
from models.actor import Actor


class Avatar(Actor):

    def _fill(self):
        for element in [x for x in self._element_set.elements if x.category == "color"]:
            self._container.add_element(element.name, element.scale.max_value)

