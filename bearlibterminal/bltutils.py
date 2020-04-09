# coding=utf-8

from bearlibterminal import terminal as blt


align_center = blt.TK_ALIGN_MIDDLE | blt.TK_ALIGN_CENTER
box_whole = 0x2580
box_upper_half = 0x2588
_lucynest_L = "\u258F[+]\u2581"
_lucynest_T = "\u2594[+]\u2595"
lucynest = _lucynest_L + "ucynes" + _lucynest_T
_tag_template = "[%s=%s]%s[/%s]"


def _tagged(tag, value, text):
    return _tag_template % (tag, value, text, tag)


def colored(text, color):
    return _tagged("color", color, text)


def bkcolored(text, color):
    return _tagged("bkcolor", color, text)


def fullcolored(text, color, bkcolor):
    return bkcolored(colored(text, color), bkcolor)


lucynest_colored = colored(lucynest, "orange")
