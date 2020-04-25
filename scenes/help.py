# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
import common.utils as utils

line = 12
offset = 10

def keybindings():

    offs = offset
    lin = line
    width = blt.state(blt.TK_WIDTH)
    half_width = int(width / 2)
    keys = (
        ("ESC", "Exit"),
        ("Enter", "Next"),
        ("PGUP", "Log up"),
        ("PGDN", "Log Down")
    )
    for (key, info) in keys:
        blt.puts(offs, lin, utils.button(key, info))
        offs = offs + half_width
        if offs > half_width + offset:
            lin = lin + 1
            offs = offset
        

def help():

    blt.set("window.title=' LucynesꞀ help'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = "Manual..."

    while True:
        blt.clear()
        
        blt.puts(0, 1, "Help", width, 1, blt.TK_ALIGN_CENTER)
        
        blt.puts(0, 0, utils.multiline_trim(info), width, line - 2, bltutils.align_center)

        blt.puts(0, line - 2, "Keybindings", width, line - 2, blt.TK_ALIGN_CENTER)
        keybindings()

        blt.puts(2, 23, utils.button_quit())

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

