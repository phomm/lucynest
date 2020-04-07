# coding=utf-8

from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
from scenes.game import game
from scenes.about import about


def reset():
    blt.set("window: size=80x25, cellsize=auto, title='LucynesT: night time';"
            "input: filter={keyboard}")
    blt.color("white")


def main():
    blt.open()

    menu_entries = (
        ("Fall asleep", game),
        ("About", about)
    )
    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    reset()
    menu_index = 0
    menu_count = len(menu_entries)
    while True:
        blt.clear()

        for (i, entry) in enumerate(menu_entries):
            bkcolor = "gray" if i == menu_index else "black"
            blt.puts(0, i, f"[bkcolor={bkcolor}] {entry[0]} [/bkcolor]", width, height // 2 + i, bltutils.align_center)

        blt.puts(2, 23, "[color=orange]ESC[/color] Exit")
        blt.refresh()

        key = blt.read()

        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break
        elif key == blt.TK_UP:
            menu_index = (menu_count + menu_index - 1) % menu_count
        elif key == blt.TK_DOWN:
            menu_index = (menu_count + menu_index + 1) % menu_count

        elif key == blt.TK_ENTER:
            menu_entries[menu_index][1]()
            reset()

    blt.close()


if __name__ == "__main__":
    main()
