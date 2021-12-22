
from typing import Tuple
import sys

def input():
    with open(sys.argv[1], 'r') as f:
        return f.read().strip()


class Scanner():
    def __init__(self, id) -> None:
        self.id = id
        self.coords = set()
        self.initial_coords: Tuple[int, int, int] = []
        self.scanners = {}
        self.no_match = {}
    
    def initial_add(self, coord: Tuple[int, int, int]):
        # print(f'Adding coord to scanner {self.id}: {coord}')
        self.coords.add(coord)
        self.initial_coords.append(coord)

    def match(self, other, perm, sign, offset) -> bool:
        s = transform_all(self.coords, perm, sign, offset) & other.coords
        count = len(s)
        # for coord in self.coords:
        #     c = transform(coord, perm, sign, offset)
        #     # print(f'match: {coord} + ({perm}, {sign}, {offset}) = {c}')
        #     if c in other.coords:
        #         count += 1
        #     if count >= 12:
        #         print(f'Scanner {self.id} matches scanner {other.id} with offset {offset} and permutations {perm} + {sign}')
        #         break
        if count < 12:
            # print(f'no match between {self.id} and {other.id}')
            self.no_match[other.id] = other
        elif other.id in self.no_match:
            del self.no_match[other.id]
        return count >= 12
    
    def add_coord(self, coord):
        # print(f'{self.id}.add_coord({coord}')
        if coord not in self.coords:
            self.coords.add(coord)
        for s, pso in self.scanners.values():
            for perm, sign, offset in pso:
                c = transform(coord, perm, sign, offset)
            if c not in s.coords:
                s.add_coord(c)

    
    # self.coord + pso -> scanner
    def register(self, scanner, pso):
        # print(f'Registering pso from scanner {self.id} to scanner {scanner.id}: {pso}')
        self.scanners[scanner.id] = (scanner, pso)
        print(f'Scanner {self.id} now knows paths to these other scanners: {list(self.scanners.keys())}')
        for c in self.coords:
            for perm, sign, offset in pso:
                c = transform(c, perm, sign, offset)
            scanner.add_coord(c)
            # coord = c
            # for perm, sign, offset in pso:
            #     c = permutate(c, perm, sign)
            #     c = apply_offset(c, offset)
            # # print(f'register coord permute: {coord} + {pso} = {c}')
            # if c not in scanner.coords:
            #     print(f' adding coord {c} in scanner {scanner.id}')
            #     scanner.coords.append(c)
            # else:
            #     print(f' not adding coord {c} in scanner {scanner.id}: already known')
        print(f'--> Scanner {scanner.id} now knows {len(scanner.coords)} coords')

        # for sid in self.scanners:
        #     # s.coord + pso2 -> self
        #     s, pso2 = self.scanners[sid]
        #     if scanner.id != s.id and scanner.id not in s.scanners:
        #         print(f'  adding path to scanner {scanner.id} into scanner {s.id}, via {self.id}')
        #         s.register(scanner, pso2+pso)  # from s to self: pso2 / from self to scanner: pso
        #     else:
        #         print(f'  scanner {scanner.id} already known by scanner {s.id}')

        # print(f'{self.id}.register({scanner.id}) done')

scanners: list[Scanner] = []
id = 0
for section in input().split('\n\n'):
    s = Scanner(id)
    scanners.append(s)
    print(f'parsing scanner {id}')
    for c in section.split('\n'):
        if c.startswith('--'):
            continue
        coord = eval(f'({c})')
        s.initial_add(coord)
    id += 1

nb_scanners = len(scanners)

def permutations(coord: Tuple[int, int, int]):
    # Too many permutaions in there: 48. Only 24 needed because x,y,z vectors
    # are ordered as an orthogonal referential and thus half of these rotations
    # are actually not valid
    perms = ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))
    signs = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    signs = signs + ((-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1))
    for p in perms:
        for s in signs:
            yield (permutate(coord, p, s), p, s)

def transform(coord, perm, sign, offset):
    return (coord[perm[0]]*sign[0]+offset[0],
            coord[perm[1]]*sign[1]+offset[1],
            coord[perm[2]]*sign[2]+offset[2])

def transform_all(coords, perm, sign, offset):
    ret = set()
    for c in coords:
        ret.add(transform(c, perm, sign, offset))
    return ret

def permutate(coord: Tuple[int, int, int], perm, sign):
    return (coord[perm[0]]*sign[0], coord[perm[1]]*sign[1], coord[perm[2]]*sign[2])

def get_offset(c1, c2):
    return (c2[0]-c1[0], c2[1]-c1[1], c2[2]-c1[2])

def apply_offset(coord, offset):
    return (coord[0]+offset[0], coord[1]+offset[1], coord[2]+offset[2])

# A better algo would be to find the correct rotation & offset and augment scanner0 only
for id, scanner in enumerate(scanners):
    # if id > 1:
    #     break
    print(f'------------------------- SCANNER {id}')
    for s in scanners:
        if s.id  == id:
            continue
        # if id in s.scanners:
        #     print(f'scanner {id} already known by {s.id}. Skipping...')
        #     continue
        if scanner.id in s.no_match:
            print(f'skipping comparison of {scanner.id} with {s.id} since no match found previoulsy')
            continue
        found_match = False
        print(f'comparing with scanner {s.id}')
        for coord in scanner.initial_coords:
            for p, perm, sign in permutations(coord):
                for c in s.initial_coords:
                    offset = get_offset(p, c)
                    if (found_match := scanner.match(s, perm, sign, offset)):
                        scanner.register(s, [(perm, sign, offset)])
                        break
                if found_match:
                    break
            if found_match:
                break

for s in scanners:
    print(f'scanner {s.id} knows {len(s.coords)} coords')
