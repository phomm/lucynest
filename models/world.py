# coding=utf-8

from models.element_set import ElementSet
from models.avatar import Avatar
from models.actor import Actor


class World:
    def __init__(self):
        self.__element_set = ElementSet()
        self.__avatar = Avatar("@", self.__element_set)

    @property
    def element_set(self):
        return self.__element_set

    @property
    def avatar(self):
        return self.__avatar

