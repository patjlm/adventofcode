with open('day2.input', 'r') as f:
  input_lines = [i for i in f.read().strip().split('\n')]

position = 0
depth = 0
aim = 0

def forward(x):
    p = position + x
    d = depth + (aim * x)
    return p, d, aim

def down(x):
    a = aim + x
    return position, depth, a

def up(x):
    a = aim - x
    return position, depth, a

for line in input_lines:
    action, count = line.split(" ")
    position, depth, aim = locals()[action](int(count))

print(position * depth)
# 1997106066
