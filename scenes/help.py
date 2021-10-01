# coding=utf-8

from __future__ import division
from bearlibterminal import bltutils, terminal as blt
from common import utils, textutils

line = 12
offset = 10


def keybindings():

    current_offset = offset
    current_line = line
    width = blt.state(blt.TK_WIDTH)
    half_width = int(width / 2)
    keys = (
        ("ESC", "Exit"),
        ("Enter", "Next"),
        ("PGUP", "Log up"),
        ("PGDN", "Log Down")
    )
    for (key, info) in keys:
        blt.puts(current_offset, current_line, utils.button(key, info))
        current_offset = current_offset + half_width
        if current_offset > half_width + offset:
            current_line = current_line + 1
            current_offset = offset


def scene():

    blt.set(f"window.title=' {textutils.lucynest} help'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    info = "Manual..."

    while True:
        blt.clear()
        
        blt.puts(0, 1, "Help", width, 1, blt.TK_ALIGN_CENTER)
        
        blt.puts(0, 0, utils.multiline_trim(info), width, line - 2, bltutils.align_center)

        blt.puts(0, line - 2, "Keybindings", width, line - 2, blt.TK_ALIGN_CENTER)
        keybindings()

        blt.puts(2, height - 2, utils.button_quit())

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break

