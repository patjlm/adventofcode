
def lines():
    with open('/Users/patmarti/dev/adventofcode/day5/day5.input', 'r') as f:
        for l in f:
            # print(l)
            c1, arrow, c2 = l.strip().split()
            x1, y1 = map(int, c1.split(','))
            x2, y2 = map(int, c2.split(','))
            # pts = list(points(x1, y1, x2, y2))
            # if len(pts) > 0:
            #     print(f'{l.strip()} : {pts[0]} - {pts[-1]} ({len(pts)})')
            #     ll = len(pts)
            #     if ll != (abs(x2-x1)+1) and ll != (abs(y2-y1)+1):
            #         print('error')
            #         exit(1)
            for pt in points(x1, y1, x2, y2):
                yield pt

def points(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        yield (x1, y1)
    elif x1 == x2:
        step = 1 if y2 > y1 else -1
        for y in range(y1, y2, step):
            yield (x1, y)
        yield (x2, y2)
    elif y1 == y2:
        step = 1 if x2 > x1 else -1
        for x in range(x1, x2, step):
            yield (x, y1)
        yield (x2, y2)
    else:
        pass
        # print('diag')

score = {}
for pt in lines():
    score[pt] = score.get(pt, 0) + 1
    print(f'{pt} -> {score[pt]}')

s = len([v for v in score.values() if v >= 2])

print(s)

# 5084
