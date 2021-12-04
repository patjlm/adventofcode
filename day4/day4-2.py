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
        self.won = False

    def addRow(self, row: int, items: List):
        for col, nb in enumerate(items):
            self._numbers[nb] = BoardNumber(nb, row, col)
    
    def call(self, called: int):
        if called in self._numbers:
            nb: BoardNumber = self._numbers[called]
            nb.call()
            self.won = all([n.called for n in self._numbers.values() if nb.row == n.row]) or \
                       all([n.called for n in self._numbers.values() if nb.col == n.col])
        return self.won

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

stop = False
last_win = None
for n in numbers:
    if stop:
        break
    for board in boards:
        if board.won:
            continue
        if board.call(n):
            last_win = (n, board)
            # is that the last board winning ?
            # no_win_boards = [b for b in boards if not b.won]
            # print(len(no_win_boards))
            # if len(no_win_boards) == 0:
            #     print(board)
            #     print(board.unmarked() * int(n))
            #     stop == True

n, board = last_win
print(f'last number: {n}')
print(f'last board: {board}')
print(board.unmarked() * int(n))

# 19* 27  96* 54* 36*
# 33* 32* 65* 11* 26*
#  0* 47* 25  59* 56*
# 41  45* 76* 14* 98 
# 52* 22* 31* 66  38*
# 8224
