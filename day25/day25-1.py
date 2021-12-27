import sys
input = open(sys.argv[1], 'r').read().strip().split('\n')
rows, cols = len(input), len(input[0])

east = {(row, col): True
        for row, line in enumerate(input) for col, char in enumerate(line)
        if char == '>'}
south = {(row, col): True
        for row, line in enumerate(input) for col, char in enumerate(line)
        if char == 'v'}

step = 0
while True:
    move_count = 0

    east2 = {}
    for row, col in east:
        new_col = 0 if col == cols - 1 else col+1
        if (row, new_col) in east or (row, new_col) in south:
            east2[(row, col)] = True
        else:
            east2[(row, new_col)] = True
            move_count += 1

    south2 = {}
    for row, col in south:
        new_row = 0 if row == rows - 1 else row+1
        if (new_row, col) in east2 or (new_row, col) in south:
            south2[(row, col)] = True
        else:
            south2[(new_row, col)] = True
            move_count += 1
    
    east, south = east2, south2

    step += 1

    if move_count == 0:
        break

print(step)
