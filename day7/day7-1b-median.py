from statistics import median
from math import floor, ceil

with open('input.txt', 'r') as f:
    line = f.read().strip()

positions = list(map(int, line.split(',')))

# https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
m = median(positions)

def fuel(target):
    f = 0
    for p in positions:
        f += abs(p - target)
    return f

f = min([fuel(floor(m)), fuel(ceil(m))])

print(f'fuel {f} for target position {m}')

# fuel 336721 for target position 316
# 336721
