from enum import IntEnum


class Status(IntEnum):
    NONE = 0
    WHITE = 1
    BLACK = 2
    PLACED_ABLE = 3


class Direction(IntEnum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8
    NONE = -1
