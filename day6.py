import collections
from typing import *

import utils

_ROOT = 'COM'



def parse_line(line: str) -> Tuple[str, str]:
    split = line.strip().split(')')
    assert len(split) == 2
    return split[0], split[1]


def to_adjacency_list(edges: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    parent_to_edges = collections.defaultdict(list)
    for e in edges:
        parent, child = e
        parent_to_edges[parent].append(child)
    return parent_to_edges


def _dfs(adjacency_list: Dict[str, List[str]],
         node: str,
         depth: int,
         func: Callable[[str, int], None]) -> None:
    children = adjacency_list.get(node, [])
    if children:
        for child in children:
            _dfs(adjacency_list, child, depth+1, func)
    func(node, depth)

def djikstra(start: str, end: str, adjacency_list: Dict[str, List[str]]) -> List[str]:
    shortest_paths = collections.defaultdict(lambda: 9e99)
    shortest_paths[start] = 0
    to_visit = {start}
    processed = set() 
    while len(to_visit):
        cur = to_visit.pop()
        for child in adjacency_list[cur]:
            shortest = shortest_paths[child]
            cur_path = shortest_paths[cur] + 1
            if cur_path < shortest:
                shortest_paths[child] = cur_path
            if child not in processed:
                to_visit.add(child)
        processed.add(cur)
    print(shortest_paths[end]-2)

def day6_pt1(lines: List[str]):
    edges = [parse_line(l) for l in lines]
    adjacency_list = to_adjacency_list(edges)
    total_orbits = [0]

    def func(node: str, depth: int):
        total_orbits[0] += depth

    _dfs(adjacency_list, _ROOT, 0, func)
    print(total_orbits[0])

def day6_pt2(lines: List[str]):
    edges = [parse_line(l) for l in lines]
    bi_edges = [ee for e in edges
                for ee in [e, (e[1], e[0])] 
                ]

    adjacency_list = to_adjacency_list(bi_edges)
    djikstra('YOU', 'SAN', adjacency_list)

utils.run(day6_pt1, 'day6_pt1.txt')
utils.run(day6_pt2, 'day6_pt2.txt')

