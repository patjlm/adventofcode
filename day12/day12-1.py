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
        self.visited = False
        self.connected: List[Cave] = []

    def __repr__(self) -> str:
        return self.name

    def visit(self, path, revisited=False):
        cur_path = path + [self]
        if self.name == 'end':
            yield cur_path
            return
        if self.small:
            self.visited = True
        for c in self.connected:
            if not c.visited:
                for p in c.visit(cur_path, revisited):
                    yield p
        self.visited = False


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

# 3708
