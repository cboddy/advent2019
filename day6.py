import collections

import utils

_ROOT = 'COM'

test = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""


def parse_line(line: str) -> Tuple[str, str]:
    split = line.strip().split(')')
    assert len(split) == 2
    return split[0], split[1]


def to_adjacency_list(edges: List[Tuple[str, str]]) -> node:
    parent_to_edges = collections.defaultdict(list)
    for e in edges:
        parent, child = e
        parent_to_edges[parent].append(child)
    return parent_to_edges


def walk(adjacency_list: Dict[str, List[str], start: str):
    cur = start
    while True:
        pass

def day6_pt1(lines: List[str]):
    edges = [parse_line(l) for l in lines]
    adjacency_list = to_adjacency_list(edges)
