import sys


def input():
    filename = sys.argv[1] if len(sys.argv) > 1 else '/Users/patmarti/dev/adventofcode/day22/test-input-1.txt' 
    with open(filename, 'r') as f:
        for l in f:
            action, cube_coords = l.strip().split(' ')
            coords = cube_coords.split(',')
            xmin, xmax = map(int, coords[0][2:].split('..'))
            ymin, ymax = map(int, coords[1][2:].split('..'))
            zmin, zmax = map(int, coords[2][2:].split('..'))
            yield (action, Cuboid((xmin, ymin, zmin), (xmax, ymax, zmax)))

class Cuboid():
    def __init__(self, coords_min, coords_max) -> None:
        self.xmin, self.ymin, self.zmin = coords_min
        self.xmax, self.ymax, self.zmax = coords_max
    
    def count_cubes(self):
        # todo, substract excludes
        return (self.xmax-self.xmin+1)*(self.ymax-self.ymin+1)*(self.zmax-self.zmin+1)

    def cubes(self):
        s = set()
        for x in range(self.xmin, self.xmax+1):
            for y in range(self.ymin, self.ymax+1):
                for z in range(self.zmin, self.zmax+1):
                    s.add((x, y, z))
        return s

    def __repr__(self) -> str:
        return str(((self.xmin, self.ymin, self.zmin), (self.xmax, self.ymax, self.zmax))) + \
            f'->{self.count_cubes()}'


def overlap_cuboid(c1, c2):
    if (c2.xmax<c1.xmin or c2.xmin>c1.xmax) or \
        (c2.ymax<c1.ymin or c2.ymin>c1.ymax) or \
        (c2.zmax<c1.zmin or c2.zmin>c1.zmax):
        return None
    return Cuboid((max(c1.xmin, c2.xmin), max(c1.ymin, c2.ymin), max(c1.zmin, c2.zmin)),
                  (min(c1.xmax, c2.xmax), min(c1.ymax, c2.ymax), min(c1.zmax, c2.zmax)))

def cuboid_for(coords):
    xmin, ymin, zmin = coords[0]
    xmax, ymax, zmax = coords[1]
    if xmin<=xmax and ymin<=ymax and zmin<=zmax:
        return Cuboid(coords[0], coords[1])
    return None

# returns a set of cuboids obtained by removing c2 from c1 
def substract(c1, c2):
    o = overlap_cuboid(c1, c2)
    if not o:
        return set((c1,))
    cuboids = set()

    # above o.zmax+1
    if (c := cuboid_for(((c1.xmin, c1.ymin, o.zmax+1), (c1.xmax, c1.ymax, c1.zmax)))):
        cuboids.add(c)

    # below o.zmin-1
    if (c := cuboid_for(((c1.xmin, c1.ymin, c1.zmin), (c1.xmax, c1.ymax, o.zmin-1)))):
        cuboids.add(c)

    # from zmin to zmax
    if c := cuboid_for(((c1.xmin, c1.ymin, o.zmin), (c1.xmax, o.ymin-1, o.zmax))):
        cuboids.add(c)
    if c := cuboid_for(((c1.xmin, o.ymax+1, o.zmin), (c1.xmax, c1.ymax, o.zmax))):
        cuboids.add(c)

    if c := cuboid_for(((c1.xmin, o.ymin, o.zmin), (o.xmin-1, o.ymax, o.zmax))):
        cuboids.add(c)
    if c := cuboid_for(((o.xmax+1, o.ymin, o.zmin), (c1.xmax, o.ymax, o.zmax))):
        cuboids.add(c)

    return cuboids

def substract_all(c1, all):
    cuboids = set((c1,))
    for c2 in all:
        if overlap_cuboid(c1, c2):
            newset = set()
            for c in cuboids:
                newset.update(substract(c, c2))
            cuboids = newset
    return cuboids

cuboids = set()
step = 0
for action, cuboid in input():
    step += 1
    if action == 'on':
        # do not count overlaping cuboids twice        
        cuboids.update(substract_all(cuboid, cuboids))
    else:
        newset = set()
        for c in cuboids:
            newset.update(substract(c, cuboid))
        cuboids = newset
    count = sum([c.count_cubes() for c in cuboids])

print(sum([c.count_cubes() for c in cuboids]))

# 1288707160324706
