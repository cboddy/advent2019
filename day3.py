import enum
from collections import namedtuple
from typing import *

import utils


class Dir(enum.Enum):
    R = enum.auto()
    L = enum.auto()
    U = enum.auto()
    D = enum.auto()


def _to_dir_and_distance(token: str) -> Tuple[Dir, int]:
    return Dir[token[0]], int(token[1:])


class Line(namedtuple('Line', ['x0', 'x1', 'y0', 'y1', 'dist', 'x_first', 'y_first'])):

    @property
    def is_horizontal(self):
        return self.y0 == self.y1

    @property
    def is_vertical(self):
        return self.x0 == self.x1

    def get_cross(self, other) -> Optional[Tuple[int, int]]:
        if self.is_vertical and other.is_vertical:
            return None
        elif self.is_horizontal and other.is_horizontal:
            return None
        elif self.is_horizontal and other.is_vertical:
            if self.x0 <= other.x0 <= self.x1 and other.y0 <= self.y0 <= other.y1:
                return other.x0, self.y0

        elif self.is_vertical and other.is_horizontal:
            if self.y0 <= other.y0 <= self.y1 and other.x0 <= self.x0 <= other.x1:
                return self.x0, other.y0
        else:
            raise ValueError()
        return None

    def get_dist(self, other) -> int:
        cross = self.get_cross(other)
        if cross is None:
            raise ValueError()
        dist = self.dist + other.dist
        cross_x, cross_y = cross
        if self.is_vertical and other.is_horizontal:
            dist += abs(self.y_first - cross_y)
            dist += abs(other.x_first - cross_x)
        elif other.is_vertical and self.is_horizontal:
            dist += abs(other.y_first - cross_y)
            dist += abs(self.x_first - cross_x)
            pass
        else:
            raise ValueError()
        return dist


def _to_lines(tokens: List[str]) -> List[Line]:
    lines = []
    x_pos, y_pos, dist = 0, 0, 0
    for token in tokens:
        _dir, distance = _to_dir_and_distance(token)
        x_pos2 = x_pos
        y_pos2 = y_pos

        if _dir == Dir.R:
            x_pos2 += distance
        elif _dir == Dir.L:
            x_pos2 -= distance
        elif _dir == Dir.U:
            y_pos2 += distance
        elif _dir == Dir.D:
            y_pos2 -= distance
        else:
            raise ValueError()
        l = Line(min(x_pos, x_pos2), max(x_pos, x_pos2),
                 min(y_pos, y_pos2), max(y_pos, y_pos2),
                 dist,
                 x_pos,
                 y_pos)
        dist += abs(x_pos2 - x_pos) + abs(y_pos2 - y_pos)
        lines.append(l)
        x_pos, y_pos = x_pos2, y_pos2
    return lines


def pt1_cost(l: Line, r: Line) -> int:
    cross = l.get_cross(r)
    return abs(cross[0]) + abs(cross[1])


def pt2_cost(l: Line, r: Line) -> int:
    return l.get_dist(r)


def day3(lines: List[str], cost: Callable[[Line, Line], int]) -> str:
    left_lines = _to_lines(lines[0].split(','))
    right_lines = _to_lines(lines[1].split(','))
    min_cost = 1e99
    for l in left_lines:
        for r in right_lines:
            cross = l.get_cross(r)
            if cross:
                _cost = cost(l, r)
                if _cost > 0:
                    min_cost = min(min_cost, _cost)
    return min_cost


def pt1(lines: List[str]) -> str:
    return day3(lines, pt1_cost)


def pt2(lines: List[str]) -> str:
    return day3(lines, pt2_cost)


utils.run(pt1, 'day3.txt')
utils.run(pt2, 'day3.txt')
