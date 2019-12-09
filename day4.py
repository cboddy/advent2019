import math

INPUT_RANGE = range(246515, 739105)


def is_valid(x: int):
    nums = [int(x//math.pow(10, pos) % 10)
            for pos in range(5, -1, -1)]

    has_adjacent = False
    for l, r in zip(nums[:-1], nums[1:]):
        if l == r:
            has_adjacent = True
        if l > r:
            # has descending
            return False
    return has_adjacent


def day4():
    print(sum(is_valid(i)
              for i in INPUT_RANGE))


day4()
