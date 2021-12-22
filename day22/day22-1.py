import sys


def input():
    with open(sys.argv[1], 'r') as f:
        for l in f:
            action, cube_coords = l.strip().split(' ')
            coords = cube_coords.split(',')
            xmin, xmax = map(int, coords[0][2:].split('..'))
            ymin, ymax = map(int, coords[1][2:].split('..'))
            zmin, zmax = map(int, coords[2][2:].split('..'))
            yield (action, ((xmin, ymin, zmin), (xmax, ymax, zmax)))

def in_50_50(cuboid):
    xmin, ymin, zmin = cuboid[0]
    xmax, ymax, zmax = cuboid[1]
    return -50<=xmin<=50 and -50<=ymin<=50 and -50<=zmin<=50 and \
           -50<=xmax<=50 and -50<=ymax<=50 and -50<=zmax<=50

def cuboid_point_set(cuboid):
    xmin, ymin, zmin = cuboid[0]
    xmax, ymax, zmax = cuboid[1]
    return {(x, y, z) for x in range(xmin, xmax+1)
                   for y in range(ymin, ymax+1)
                   for z in range(zmin, zmax+1)}

s = set()
for action, cuboid in input():
    if in_50_50(cuboid):
        print(action, cuboid)
        if action == 'on':
            s |= cuboid_point_set(cuboid)
        else:
            s -= cuboid_point_set(cuboid)
    print(len(s))

print(len(s))
