from dataclasses import dataclass

def parse():
    with open('/Users/patmarti/dev/adventofcode/day11/input.txt', 'r') as f:
        for line in f:
            yield line.strip()


@dataclass
class Octopus():
    energy: int
    row: int
    col: int
    flashed: bool = False

    def incr(self):
        self.energy += 1
        if self.energy > 9:
            self.flash()

    def flash(self):
        if self.flashed:  # already done
            return
        self.flashed = True
        for row in range(max(0, self.row-1), min(self.rows, self.row+2)):
            for col in range(max(0, self.col-1), min(self.cols, self.col+2)):
                matrix[row][col].incr()


matrix = []

row = 0
for line in parse():
    matrix.append([Octopus(int(o), row, col) for col, o in enumerate(line)])
    row += 1

rows = len(matrix)
cols = len(matrix[0])
matrix_size = rows * cols

step = 0
while True:
    step += 1
    step_flashes = 0
    for row, octopuses in enumerate(matrix):
        for col, octopus in enumerate(octopuses):
            octopus.energy += 1
            octopus.rows = rows
            octopus.cols = cols

    for row, octopuses in enumerate(matrix):
        for col, octopus in enumerate(octopuses):
            if octopus.energy > 9:
                octopus.flash()

    for row, octopuses in enumerate(matrix):
        for col, octopus in enumerate(octopuses):
            if octopus.flashed:
                step_flashes +=1
                octopus.flashed = False
                octopus.energy = 0
    
    if step_flashes == matrix_size:
        break

print(step)

# 382
