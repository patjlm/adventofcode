with open('day2.input', 'r') as f:
  input_lines = [i for i in f.read().strip().split('\n')]

position = 0
depth = 0
aim = 0

for line in input_lines:
    action, count = line.split(" ")
    count = int(count)
    if (action == 'forward'):
        position += count
        depth += aim * count
    elif (action == 'down'):
        aim += count
    elif (action == 'up'):
        aim -= count

print(position * depth)
# 1997106066
