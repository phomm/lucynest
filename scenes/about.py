# coding=utf-8

from __future__ import division
from bearlibterminal import bltutils, terminal as blt
from common import utils, textutils


def scene():

    blt.set(f"window.title=' About {textutils.lucynest}'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = f'''{textutils.lucynest_colored}
            
            It is when you are in lucid dream
            Open Your mind to go through it and find yourself'''

    while True:
        blt.clear()
        blt.puts(0, 0, utils.multiline_trim(info), width, height, bltutils.align_center)
        blt.puts(2, 23, utils.button_quit())

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

