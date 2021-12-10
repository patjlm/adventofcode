from  dataclasses import dataclass
from typing import List


@dataclass
class Point():
    height: int
    row: int
    col: int
    basin: bool = False

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

    def discover_basin(self, point_map):
        if self.height == 9:
            return 0
        self.basin = True
        size = 1
        for adj in self.adjacents(point_map):
            if not adj.basin:
                size += adj.discover_basin(point_map)
        return size


def parse() -> List[Point]:
    with open('/Users/patmarti/dev/adventofcode/day9/input.txt', 'r') as f:
        row = 0
        for line in f:
            yield [Point(int(p), row, col) for col, p in enumerate(line.strip())]
            row += 1

point_map = [l for l in parse()]

basin_sizes = []
for points in point_map:
    for point in points:
        if point.height < 9 and not point.basin:
            basin_sizes.append(point.discover_basin(point_map))

sizes = sorted(basin_sizes, reverse=True)
result = sizes[0] * sizes[1] * sizes[2]

print(result)

# 1142757
