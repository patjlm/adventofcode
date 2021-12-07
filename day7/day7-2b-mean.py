from statistics import mean
from math import floor, ceil

with open('input.txt', 'r') as f:
    line = f.read().strip()

positions = list(map(int, line.split(',')))

m = mean(positions)

def fuel(target):
    f = 0
    for p in positions:
        n = abs(p - target)
        f += int(n*(n+1)/2)
    return f

f = min([fuel(floor(m)), fuel(ceil(m))])

print(f'fuel {f} for target position {m}')

# fuel 336721 for target position 316
# 336721
