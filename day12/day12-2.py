from typing import List, Mapping
import sys

def parse():
    with open('/Users/patmarti/dev/adventofcode/day12/input.txt', 'r') as f:
        for line in f:
            yield line.strip().split('-')


class Cave():
    def __init__(self, name: str) -> None:
        self.name = name
        self.small = name.lower() == name
        self.visited = 0
        self.connected: List[Cave] = []

    def __repr__(self) -> str:
        return f'{self.name}({self.visited})'

    def visit(self, path, revisited=False):
        cur_path = path + [self]
        if self.name == 'end':
            yield cur_path
            return
        revisited = revisited or self.visited > 0
        if self.small:
            self.visited += 1
        for c in self.connected:
            if c.name != 'start' and (c.visited == 0 or not revisited):
                for p in c.visit(cur_path, revisited):
                    yield p
        if self.small:
            self.visited -= 1


caves: Mapping[str, Cave] = {}

for f, t in parse():
    f_cave = caves.setdefault(f, Cave(f))
    t_cave = caves.setdefault(t, Cave(t))
    f_cave.connected.append(t_cave)
    t_cave.connected.append(f_cave)

count = 0
for path in caves['start'].visit([]):
    count += 1

print(count)

# 93858
