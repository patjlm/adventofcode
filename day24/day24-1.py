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
    # print(f'run(..., {w}, {x}, {y}, {z}, {input_value})')
    vars = {'w':0, 'x':0, 'y':0, 'z':z}
    inp(instructions[0][1], vars, input_value)
    for instr, v1, v2 in instructions[1:]:
        # print(instr, v1, v2, vars)
        ok = globals()[instr](v1, v2, vars)
        # print(f'ok={ok}', vars)
        if not ok:
            return None
        # w, x, y, z = [vars[i] for i in ('w', 'x', 'y', 'z')]
    return vars['z']

# test_numbers = tuple(range(9, 0, -1))

@functools.lru_cache(maxsize=None)
def search_max(instructions_id=0, z0=0):
    for n in range(9, 0, -1):
        if instructions_id <= 4:
            prefix = ' '*(instructions_id)
            print(prefix, n, 'search_max: ', instructions_id, z0, search_max.cache_info())
        z = run(instructions[instructions_id], z0, n)
        if z is None:  # invalid instruction (divide by 0)
            continue
        if instructions_id == len(instructions)-1:
            return [n] if z == 0 else None
        # print(f'{leading_numbers} + {n}: search_max({len(instructions)}, {input_vars})')
        # x and y are always reset to 0, w is always the input
        numbers = search_max(instructions_id+1, z)
        if numbers:
            return [n] + numbers
    return None

numbers = search_max()

if not numbers:
    print('ERROR: nothing valid found')

print(numbers)
