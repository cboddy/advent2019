import math
from typing import *

INPUT_RANGE = range(246515, 739105)


def _nums(x: int):
    return [int(x//math.pow(10, pos) % 10)
            for pos in range(5, -1, -1)]


def pt1_valid(nums: List[int]):
    has_adjacent = False
    for l, r in zip(nums[:-1], nums[1:]):
        if l == r:
            has_adjacent = True
        if l > r:
            # has descending
            return False
    return has_adjacent


def pt2_valid(nums: List[int]):
    has_adjacent = False
    for idx, (l, r) in enumerate(zip(nums[:-1], nums[1:])):
        if l == r and not has_adjacent:
            has_adjacent = True
            if idx > 0 and nums[idx-1] == l:
                has_adjacent = False
            if idx < len(nums) - 2 and nums[idx+2] == l:
                has_adjacent = False
        if l > r:
            # has descending
            return False
    return has_adjacent


def day4():
    print(sum(pt1_valid(_nums(i))
              for i in INPUT_RANGE))
    print(sum(pt2_valid(_nums(i))
              for i in INPUT_RANGE))


day4()
