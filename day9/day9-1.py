from  dataclasses import dataclass
from typing import List


@dataclass
class Point():
    height: int
    lowest: bool = False

    def adjacents(self, current, previous, col):
        adj = []
        if previous:
            adj.append(previous[col])
        if col > 0:
            adj.append(current[col-1])
        if col < len(current)-1:
            adj.append(current[col+1])
        return adj


def parse() -> List[Point]:
    with open('/Users/patmarti/dev/adventofcode/day9/input.txt', 'r') as f:
        for line in f:
            yield [Point(int(p)) for p in line.strip()]

previous = None
current  = None
risk = 0
for points in parse():
    current = points
    for col, p in enumerate(points):
        if previous:
            prev = previous[col]
            prev.lowest = prev.lowest and prev.height < p.height
            if prev.lowest:
                risk += prev.height + 1
        adj = p.adjacents(points, previous, col)
        p.lowest = all([p.height < a.height for a in adj])
    previous = points

for p in current:
    if p.lowest:
        risk += p.height + 1

print(risk)

# 537
