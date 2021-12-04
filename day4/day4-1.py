from typing import List

class BoardNumber():
    def __init__(self, nb, row, col) -> None:
        self.nb = nb
        self.row = row
        self.col = col
        self.called = False
    
    def call(self):
        self.called = True

    def __repr__(self):
        star = '*' if self.called else ' '
        return f'{int(self.nb):2}{star}'


class Board():
    def __init__(self):
        self._numbers = {}

    def addRow(self, row: int, items: List):
        for col, nb in enumerate(items):
            self._numbers[nb] = BoardNumber(nb, row, col)
    
    def call(self, called: int):
        win = False
        if called in self._numbers:
            nb: BoardNumber = self._numbers[called]
            nb.call()
            return all([n.called for n in self._numbers.values() if nb.row == n.row]) or \
                   all([n.called for n in self._numbers.values() if nb.col == n.col])
        return win

    def unmarked(self):
        return sum([int(nb.nb) for nb in self._numbers.values() if not nb.called])

    def __str__(self):
        rows = []
        for row in range(5):
            nb = sorted(
                    [n for n in self._numbers.values() if n.row == row],
                    key=lambda n: n.col)
            rows.append(' '.join(map(str, nb)))
        return '\n' + '\n'.join(rows)

boards = []

with open('/Users/patmarti/dev/adventofcode/day4/day4.input', 'r') as f:
    numbers = f.readline().strip().split(',')
    for line in f:
        if line.strip():
            board.addRow(row, line.strip().split())
            row += 1
        else:
            board = Board() 
            boards.append(board)
            row = 0

win = False
for n in numbers:
    pass
    if win:
        break
    for board in boards:
        win = board.call(n)
        if win:
            print(n)
            print(board)
            print(f'sum = {board.unmarked()}')
            print(board.unmarked() * int(n))
            break

# 28082
