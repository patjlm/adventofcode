def parse_coord():
    with open('/Users/patmarti/dev/adventofcode/day13/input.txt', 'r') as f:
        for line in f:
            if ',' in line:
                yield map(int, line.strip().split(','))

def parse_fold():
    with open('/Users/patmarti/dev/adventofcode/day13/input.txt', 'r') as f:
        for line in f:
            if 'fold' in line:
                axe, id = line.strip()[len('fold along '):].split('=')
                yield (axe, int(id))

dots = {}

for x, y in parse_coord():
    dots[(x, y)] = True

def idx(axe, dot):
    return dot[0] if axe == 'x' else dot[1]

def folded(axe, folding, dot):
    if idx(axe, dot) > 2*folding:
        return None
    if axe == 'x':
        return (2*folding-dot[0], dot[1])
    else:
        return (dot[0], 2*folding-dot[1])

for axe, folding in parse_fold():
    for dot in list(dots.keys()):
        id = idx(axe, dot)
        if id > folding:
            new_dot = folded(axe, folding, dot)
            if new_dot:
                dots[new_dot] = True
                dots.pop(dot, None)

max_x = max([d[0] for d in dots])
max_y = max([d[1] for d in dots])
for y in range(max_y+1):
    print(''.join(['#' if (x, y) in dots else ' ' for x in range(max_x+1)]))        

#  ##    ##  ##  #  # ###   ##  ###  ###
# #  #    # #  # # #  #  # #  # #  # #  #
# #       # #    ##   ###  #  # #  # ###
# #       # #    # #  #  # #### ###  #  #
# #  # #  # #  # # #  #  # #  # #    #  #
#  ##   ##   ##  #  # ###  #  # #    ###
#
# -> CJCKBAPB
