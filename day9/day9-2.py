from  dataclasses import dataclass
from typing import Any, List
import sys

class Basin():
    
    def __init__(self, id: int) -> None:
        self.id = id
        self.points = []

    def __str__(self):
        return f'{self.id}({len(self.points)})'

    def __repr__(self):
        return f'{self.id}({len(self.points)})'

    def add(self, point):
        self.points.append(point)


@dataclass
class Point():
    height: int
    row: int
    col: int
    lowest: bool = False
    basin: Basin = None

    def __str__(self):
        return f'({self.row},{self.col})'

    def __repr__(self):
        return f'({self.row},{self.col})'

    def adjacents(self, point_map):
        adj = []
        if self.row > 0:
            adj.append(point_map[self.row-1][self.col])
        if self.row < len(point_map)-1:
            adj.append(point_map[self.row+1][self.col])
        if self.col > 0:
            adj.append(point_map[self.row][self.col-1])
        if self.col < len(point_map[self.row])-1:
            adj.append(point_map[self.row][self.col+1])
        return adj

    def discover_basin(self, basin: Basin, point_map):
        if self.height == 9:
            return
        if self.basin:
            raise Exception(f'Point already in a basin {self.basin}: {self}')
        self.basin = basin
        basin.add(self)
        for adj in self.adjacents(point_map):
            if adj.basin:
                if adj.basin.id == basin.id: # already in that basin
                    continue
                else:
                    raise Exception(f'Point {adj} already in a basin {adj.basin}. '
                                    f'Cannot be added in basin {basin}')
            adj.discover_basin(basin, point_map)


def parse() -> List[Point]:
    with open('/Users/patmarti/dev/adventofcode/day9/input.txt', 'r') as f:
        row = 0
        for line in f:
            yield [Point(int(p), row, col) for col, p in enumerate(line.strip())]
            row += 1

point_map = [l for l in parse()]

basins = []
for row, points in enumerate(point_map):
    for col, point in enumerate(points):
        if point.height < 9 and point.basin is None:
            basin = Basin(len(basins))
            basins.append(basin)
            point.discover_basin(basin, point_map)

for i, b in enumerate(basins):
    print(f'basin {i+1}: {len(b.points)}')

sorted_basins = sorted(basins, key=lambda b: len(b.points), reverse=True)
result = len(sorted_basins[0].points) * \
         len(sorted_basins[1].points) * \
         len(sorted_basins[2].points)

print(f'{len(sorted_basins[0].points)}, {len(sorted_basins[1].points)}, {len(sorted_basins[2].points)}')
print(result)

# 1142757
