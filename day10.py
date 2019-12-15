import collections
import enum
import math
from typing import *

import utils


class Space(enum.Enum):
    EMPTY = '.'
    ASTEROID = '#'


class SpacePos(collections.namedtuple('SpacePos', ['x', 'y', 'space'])):
    def angle(self, other):
        return math.atan2(self.x - other.x, self.y - other.y)


def parse(lines: List[str]) -> List[SpacePos]:
    return [SpacePos(x, y, Space(char))
            for y, line in enumerate(lines)
            for x, char in enumerate(line.strip())
            ]


def angle(_from: Tuple[int, int], _to: Tuple[int, int]) -> float:
    """
    x....
    .....
    ..x..

    tan(a) = dy/dx
    """
    dx = _from[0] - _to[0]
    dy = _from[1] - _to[1]
    return math.atan2(dx, dy)


def day9_pt1():
    lines = utils._read_all('day10.txt')
    spaces = parse(lines)
    asteroids =  [s for s in spaces if s.space == Space.ASTEROID]
    angles = []
    max_angles = 0
    best_pos = None

    for space_l in asteroids:
        angles = []
        for space_r in asteroids:
            if space_l == space_r:
                continue
            angle = space_l.angle(space_r)
            angles.append(angle)
        distinct_angles = len(set(angles))
        if distinct_angles > max_angles:
            max_angles = distinct_angles
            best_pos = space_l
    print(max_angles)


day9_pt1()
