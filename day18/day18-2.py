from math import ceil
import json
from typing import Tuple

def input():
    with open('/Users/patmarti/dev/adventofcode/day18/input.txt', 'r') as f:
        for l in f:
            yield json.loads(l)

def isint(i):
    return isinstance(i, int)


class Element():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.is_pair = False

    def __repr__(self) -> str:
        return str(self.value)

    def parent_count(self):
        p = self.parent
        count = 0
        while p:
            count += 1
            p = p.parent
        return count
    
    def explode(self):
        return False

    def split(self):
        if self.value >= 10:
            left = Element(int(self.value / 2))
            right = Element(ceil(self.value / 2))
            p = add(left, right)
            setparent(p, self.parent)
            return True, p
        return False, self
    
    def magnitude(self):
        return self.value


class Pair(Element):
    def __init__(self, left, right):
        super().__init__(None)
        self.left = left
        self.right = right
        self.is_pair = True

    def __repr__(self) -> str:
        return f'[{self.left},{self.right}]'

    def explode_left(self) -> Element:
        p = self.parent
        child = self
        while p and p.right != child:
            child = p
            p = p.parent
        if p:
            child = p.left
            while child.is_pair:
                child = child.right
            return child
        return None

    def explode_right(self) -> Element:
        p = self.parent
        child = self
        while p and p.left != child:
            child = p
            p = p.parent
        if p:
            child = p.right
            while child.is_pair:
                child = child.left
            return child
        return None

    def is_left_child(self):
        return self.parent is not None and self.parent.left == self

    def explode(self):
        if self.parent_count() < 4:
            # explode left first, then right if nothing done on left
            return self.left.explode() or self.right.explode()
        left_elt = self.explode_left()
        right_elt = self.explode_right()
        if left_elt: # Elt found on left
            left_elt.value += self.left.value
        if right_elt: # Elt found on right
            right_elt.value += self.right.value
        if self.is_left_child():
            e = Element(0)
            self.parent.left = e
            setparent(e, self.parent)
        else:
            e = Element(0)
            self.parent.right = e
            setparent(e, self.parent)
        return True

    def split(self):
        has_split, self.left = self.left.split()
        if not has_split:
            has_split, self.right = self.right.split()
        return has_split, self

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

def setparent(a, b):
    if not isint(a):
        a.parent = b

def add(a, b):
    p = Pair(a, b)
    setparent(a, p)
    setparent(b, p)
    return p

def parse(arr):
    if isint(arr):
        return Element(arr)
    left = parse(arr[0])
    right = parse(arr[1])
    p = add(left, right)
    return p

def reduce(a):
    return a.explode() or a.split()[0]

def add_all(numbers):
    previous = None
    for a in numbers:
        cur = parse(a)
        if not previous:
            previous = cur
            continue
        res = add(previous, cur)
        previous = res
        while reduce(previous):
            pass
    return previous

numbers = list(input())
max_magnitude = 0
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers):
        if j != i:
            res = add_all([a, b])
            max_magnitude = max(max_magnitude, res.magnitude())
print(max_magnitude)

# 4647
