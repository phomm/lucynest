from itertools import repeat


def multiline_trim(input_string, trim_symbols=None, before=True, after=True):
    trim_funcs = {
        (True, True): str.strip, (False, False): lambda s, _: s,
        (True, False): str.lstrip, (False, True): str.rstrip
    }
    return str.join("\n", map(trim_funcs[(before, after)], input_string.split("\n"), repeat(trim_symbols or ' ')))


def circulate(count: int, current: int, to_end: bool):
    return (count + current + (1 if to_end else -1)) % count


def button_quit():
    return "[color=orange]ESC[/color] Back"
