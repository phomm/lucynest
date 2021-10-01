# coding=utf-8

from common import utils
from bearlibterminal import bltutils

styled_L = "\u258F[+]\u2581"
styled_T = "\u2594[+]\u2595"
__button_colored_fmt = "[color=orange]%s[/color] %s"


def styled(text):
    return styled_L + text + styled_T


def button_styled():
    pass


lucynest = "LucynesꞀ"
lucynest_styled = styled("ucynes")
lucynest_colored = bltutils.colored(lucynest_styled, "orange")


