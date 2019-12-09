from typing import *


def run(func: Callable[[List[str]], str],
        f_path: str):
    with open(f_path, "r") as f:
        lines = f.readlines()
    print(func(lines))
