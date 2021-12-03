with open('day2.input', 'r') as f:
  input_lines = [i for i in f.read().strip().split('\n')]

position = 0
depth = 0
for line in input_lines:
    action, count = line.split(" ")
    count = int(count)
    if (action == 'forward'):
        position += count
    elif (action == 'down'):
        depth += count
    elif (action == 'up'):
        depth -= count

print(position * depth)
# 1936494
