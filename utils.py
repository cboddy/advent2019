from typing import *


def _read_all(f_path: str) -> List[str]:
    with open(f_path, "r") as f:
        return f.readlines()


def _read_one(f_path:  str) -> str:
    return _read_all(f_path)[0]


def run(func: Callable[[List[str]], str],
        f_path: str):
    lines = _read_all(f_path)
    print(func(lines))
