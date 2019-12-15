import collections
from typing import *

import utils


class Node(collections.namedtuple('Node', ['children', 'metadata'])):
    def metadata_sum(self):
        total = 0
        total += sum(self.metadata)
        for c in self.children:
            total += c.metadata_sum()
        return total

    def meta_metadata_sum(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        total = 0
        for idx in self.metadata:
            if idx == 0:
                continue
            if idx > len(self.children):
                continue
            total += self.children[idx-1].meta_metadata_sum()

        return total


def parse(line: List[int], pos: int = 0) -> Tuple[Node, int]:
    """returns the parsed Node and the final position"""
    n_children, n_metadata = int(line[pos]),  int(line[pos+1])
    pos += 2
    children = []
    for child in range(n_children):
        node, last_pos = parse(line, pos)
        pos = last_pos
        children.append(node)
    metadata = line[pos: pos + n_metadata]

    node = Node(children, metadata)
    return node, pos + n_metadata


def test_sums():
    line = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    node, pos = parse(line)
    assert 138 == node.metadata_sum()
    assert 66 == node.meta_metadata_sum()


def day8():
    lines = [[int(i) for i in line.split()]
             for line in utils._read_all('day8_2018.txt')]
    nodes = [parse(line)
             for line in lines]
    # pt1
    total = sum(n.metadata_sum() for n, _ in nodes)
    print(total)
    # pt2
    total = sum(n.meta_metadata_sum() for n, _ in nodes)
    print(total)


day8()
