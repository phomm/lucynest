# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
import common.utils as utils


def help():

    blt.set("window.title=' LucynesꞀ help'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = "Manual, keybindings..."

    while True:
        blt.clear()
        blt.puts(0, 0, utils.multiline_trim(info), width, height, bltutils.align_center)
        blt.puts(2, 23, utils.button_quit())

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

