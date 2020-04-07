def circulate(count: int, current: int, to_end: bool):
    return (count + current + 1 if to_end else -1) % count
