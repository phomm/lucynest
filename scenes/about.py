# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
import common.utils as utils


def about():

    blt.set("window.title=' About LucynesꞀ'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = f'''{bltutils.lucynest_colored}
            
            It is when you are in lucid dream
            Open Your mind to go through it and find yourself'''

    while True:
        blt.clear()
        blt.puts(0, 0, utils.multiline_trim(info), width, height, bltutils.align_center)
        blt.puts(2, 23, "[color=orange]ESC[/color] Back")

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

