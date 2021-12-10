def parse():
    with open('/Users/patmarti/dev/adventofcode/day10/input.txt', 'r') as f:
        for line in f:
            yield line.strip()

pairs = { ')': '(', ']': '[', '}': '{', '>': '<' }
points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

score = 0

for line in parse():
    opened = []
    for c in line:
        if c in '([{<':
            opened.append(c)
        else:
            last_opened = opened.pop()
            if pairs[c] != last_opened:
                score += points[c]
                break

print(score)
