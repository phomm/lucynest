# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
from collections import namedtuple
import common.utils as utils


def game():
    blt.set("window.title='LucynesꞀ: in a dream'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)
    parts = 6
    left = width // 6
    right = width * (parts - 1) // parts
    middle = height // 2
    padding = 1

    story = [
        "Hi! I'm Avatar, actually me is who You are in this World",
        "Lets find out what we've got here in lucid dream",
        "Open Your mind and enter this evershining mental landscape",
    ]
    story_point = 0
    while True:
        blt.clear()

        blt.color("light gray")
        for y in range(height - 1):
            blt.put(left, y, bltutils.box_upper_half)
            blt.put(right, y, bltutils.box_upper_half)
        for x in range(left + 1, right):
            blt.put(x, middle, bltutils.box_whole)

        blt.color("white")
        # blt.put_ext(view_width * 4 + 1, 0, margin, margin, 0xE100)
        avatar_symbol = "@:"
        left_avatar = left + 1 + padding
        left_avatar_text = left_avatar + len(avatar_symbol) + 1

        blt.puts(left_avatar, middle // 5, f"[color=orange]{avatar_symbol}[/color]")
        blt.puts(left_avatar_text, middle // 5, f"{story[story_point]}",
                 right - 1 - padding - left_avatar_text, middle - 1 - padding - middle // 5,
                 blt.TK_ALIGN_LEFT)

        blt.puts(2, 23, utils.button("ESC", "Menu"))

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break
        elif key == blt.TK_ENTER:
            story_point += 1 if story_point < len(story) - 1 else 0


def keys_footer():
    height = blt.state(blt.TK_HEIGHT) - 1
    keys = (
        ("ESC", "Exit"),
        ("Enter", "Next"),
        ("PGUP", "Log up"),
        ("PGDN", "Log Down")
    )
    offset = 0
    for (key, info) in keys:
        blt.puts(offset, height, f"[bkcolor=grey][color=yellow]{key}[/color] [color=black]{info}[/color][/bkcolor]")
        offset += 2 + len(key) + len(info)


