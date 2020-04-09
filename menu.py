# coding=utf-8

from bearlibterminal import terminal as blt
from bearlibterminal import bltutils
from scenes.game import game
from scenes.help import help
from scenes.about import about
import common.utils as utils


def reset():
    blt.set("window: size=80x25, cellsize=auto, title='LucynesꞀ: night time';"
            "input: filter={keyboard}")
    blt.color("white")


def main():
    version = "v0.1.0"

    blt.open()

    menu_entries = (
        ("Fall asleep", game),
        ("Help", help),
        ("About", about),
        ("Quit", quit)
    )
    
    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)

    cw = blt.state(blt.TK_CELL_WIDTH)
    ch = blt.state(blt.TK_CELL_HEIGHT)
    blt.set("U+E001: resources/logo.png, resize=" + str(cw * 70) + "x" + str(ch * 8) + ", resize-filter=bilinear")

    reset()
    menu_index = 0
    menu_count = len(menu_entries)
    while True:
        blt.clear()

        blt.put(5, 5, 0xE001)
        blt.puts(60, 11, bltutils.colored(version, "orange"))

        for (i, entry) in enumerate(menu_entries):
            bkcolor = "gray" if i == menu_index else "black"
            item_ypos = ((height // 3) * 3) + i + 3
            blt.puts(0, i, bltutils.bkcolored(entry[0], bkcolor), width, item_ypos, bltutils.align_center)

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break
        elif key in (blt.TK_UP, blt.TK_DOWN):
            menu_index = utils.circulate(menu_count, menu_index, key == blt.TK_DOWN)

        elif key == blt.TK_ENTER:
            menu_entries[menu_index][1]()
            reset()

    blt.close()


if __name__ == "__main__":
    main()
