# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
import common.utils as utils

y = 12
x = 2

def keybindings():

    i = x
    j = y
    width = blt.state(blt.TK_WIDTH)
    h = int(width / 2)
    keys = (
        ("ESC", "Exit"),
        ("Enter", "Next"),
        ("PGUP", "1Log up"),
        ("PGUP", "2Log up"),
        ("PGUP", "3Log up"),
        ("PGUP", "4Log up"),
        ("PGUP", "5Log up"),
        ("PGUP", "6Log up"),
        ("PGUP", "7Log up"),
        ("PGDN", "8Log Down")
    )
    offset = 0
    for (key, info) in keys:
        blt.puts(i, j, utils.button(key, info))
        i = i + h + x
        if i > h + x + x:
            j = j + 1
            i = x
        

def help():

    blt.set("window.title=' LucynesꞀ help'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = "Manual..."

    while True:
        blt.clear()
        
        blt.puts(0, 1, "Help", width, 1, blt.TK_ALIGN_CENTER)
        
        blt.puts(0, 0, utils.multiline_trim(info), width, y - 2, bltutils.align_center)

        blt.puts(0, y - 2, "Keybindings", width, y - 2, blt.TK_ALIGN_CENTER)
        keybindings()

        blt.puts(2, 23, utils.button_quit())

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

