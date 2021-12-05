
def lines():
    with open('/Users/patmarti/dev/adventofcode/day5/day5.input', 'r') as f:
        for l in f:
            c1, arrow, c2 = l.strip().split()
            x1, y1 = map(int, c1.split(','))
            x2, y2 = map(int, c2.split(','))
            for pt in points(x1, y1, x2, y2):
                yield pt

def points(x1, y1, x2, y2):
    stepx = 0 if x1 == x2 else int((x2-x1) / abs(x2-x1))
    stepy = 0 if y1 == y2 else int((y2-y1) / abs(y2-y1))
    x, y = x1, y1
    while x != x2 or y != y2:
        yield (x, y)
        x += stepx
        y += stepy
    yield (x2, y2)


score = {}
for pt in lines():
    score[pt] = score.get(pt, 0) + 1

s = len([v for v in score.values() if v >= 2])

print(s)

# 17882
