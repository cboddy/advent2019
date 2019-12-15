from typing import *

import utils

WIDTH = 25
DEPTH = 6
AREA = WIDTH*6


def day8_pt1(line: str):
    line = [int(i) for i in line.strip()]
    min_zero = AREA
    for pos in range(0, len(line), AREA):
        layer = line[pos: pos+AREA]
        n_zero = sum(1 for i in layer if i == 0)
        if n_zero < min_zero:
            min_zero = n_zero
            target = sum(1 for i in layer if i == 1) * sum(1 for i in layer if i == 2)
    print(target)


def day8_pt2(line: str):
    line = [int(i) for i in line.strip()]
    final_image = [2]*AREA
    for pos in range(0, len(line), AREA):
        layer = line[pos: pos+AREA]
        for idx, value in enumerate(layer):
            if final_image[idx] == 2 and value != 2:
                final_image[idx] = value

    for pos in range(0, len(final_image), WIDTH):
        print(''.join('*' if v else ' ' for v in final_image[pos:pos+WIDTH]))


day8_pt1(utils._read_one('day8.txt'))
day8_pt2(utils._read_one('day8.txt'))
