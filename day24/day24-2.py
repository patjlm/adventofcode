# This implementation fails... it's way too long.. and does not output a valid result for some reason

import sys
import functools
from collections import defaultdict

instructions = []
with open(sys.argv[1], 'r') as f:
    previous = None
    for l in f:
        s = l.strip().split()
        if s[0] == 'inp':
            if previous:
                instructions.append(tuple(previous))
            previous = [(s[0], s[1], None)]
        else:
            instr, v1, v2 = s
            previous.append((instr, v1, v2))
instructions.append(tuple(previous))
instructions = tuple(instructions)

# print(instructions)

# inp a - Read an input value and write it to variable a.
def inp(a, vars, value):
    vars[a] = value
    return True
# add a b - Add the value of a to the value of b, then store the result in variable a.
def add(a, b, vars):
    vars[a] += int(vars.get(b, b))
    return True
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
def mul(a, b, vars):
    vars[a] *= int(vars.get(b, b))
    return True
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
def div(a, b, vars):
    if int(vars.get(b, b)) == 0:
        return False
    # assert vars[a] >= 0
    # assert int(vars.get(b, b)) > 0
    vars[a] = vars[a] // int(vars.get(b, b))
    return True
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
def mod(a, b, vars):
    vars[a] = vars[a] % int(vars.get(b, b))
    return True
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
def eql(a, b, vars):
    vars[a] = int(vars[a] == int(vars.get(b, b)))
    return True

# @functools.lru_cache(maxsize=None)
def run(instructions, z, input_value):
    vars = {'w':0, 'x':0, 'y':0, 'z':z}
    inp(instructions[0][1], vars, input_value)
    for instr, v1, v2 in instructions[1:]:
        ok = globals()[instr](v1, v2, vars)
        if not ok:
            return None
    return vars['z']

def run2(instr_id, z, w):
    params = [
        (11, 8, 1),
        (14, 13, 1),
        (10, 2, 1),
        (0, 7, 26),
        (12, 11, 1),
        (12, 4, 1),
        (12, 13, 1),
        (-8, 13, 26),
        (-9, 10, 26),
        (11, 1, 1),
        (0, 2, 26),
        (-5, 14, 26),
        (-6, 6, 26),
        (-12, 14, 26),
    ]
    addx, addy, div = params[instr_id]
    z = z//div if w == (z%26) + addx else (26*z//div) + w + addy
    return z

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()
def spin(first=False):
    if not first:
        sys.stdout.write('\b')
    sys.stdout.write(next(spinner))
    sys.stdout.flush()

@functools.lru_cache(maxsize=None)
def search_max(instructions_id=0, z0=0):
    if instructions_id <= 4:
        spin()

    for n in range(10):
        z = run2(instructions_id, z0, n)
        if z is None:  # invalid instruction (divide by 0)
            print('invalid instruction')
            continue
        if instructions_id == len(instructions)-1:
            if z == 0:
                return [n]
        else:
            numbers = search_max(instructions_id+1, z)
            if numbers:
                return [n] + numbers
    return None

spin(first=True)
numbers = search_max()

print('')
if not numbers:
    print('ERROR: nothing valid found')

print(''.join(map(str, numbers)))

# 51131616112781
