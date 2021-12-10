import statistics
from math import ceil

def parse():
    with open('/Users/patmarti/dev/adventofcode/day10/input.txt', 'r') as f:
        for line in f:
            yield line.strip()

closing = { ')': '(', ']': '[', '}': '{', '>': '<' }
opening = {v: k for k, v in closing.items()}
points = { ')': 1, ']': 2,  '}': 3, '>': 4 }

scores = []

for line in parse():
    opened = []
    score = 0
    incomplete = True
    for c in line:
        if c in '([{<':
            opened.append(c)
        else:
            last_opened = opened.pop()
            if closing[c] != last_opened:
                incomplete = False
                break
    if incomplete:
        completion = [opening[c] for c in reversed(opened)]
        for c in completion:
            score *= 5
            score += points[c]
        scores.append(score)

print(sorted(scores)[ceil(len(scores)/2)])

# 2776842859
