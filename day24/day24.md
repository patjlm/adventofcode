# Solving this manually !

# Pattern

Each instruction set follows the same pattern !

inp w

mul x 0
add x z
mod x 26
add x {addx} -> x = z%26+{addx}
eql x w
eql x 0 -> x = 0 if w == z%26+{addx}, else 1

mul y 0  -> y=0
add y 25 -> y=25
mul y x  -> y=25x = 0 if w == z%26+{addx}, else 25
add y 1  -> y=1 if w == z%26+{addx}, else 26

div z {div} -> z = z//{div}
mul z y     -> z = yz//{div} = z//{div} if w == z%26+{addx}, else 26z//{div} => 26z or z

mul y 0
add y w  -> y=w
add y {addy}  -> y=w+{addy}
mul y x  -> y = 0 if w == z%26+{addx}, else w+{addy}

add z y -> z = z//{div} if w == z%26+{addx}, else 26z//{div} + w+{addy}

So overall, the pattern for each instruction set is:
- get input params for w (1<=w<=9) and previous value of z as well as a `addx`, `addy` and `div` params
- the compute z with `z = z//{div} if w == z%26+{addx} else 26z//{div} + w+{addy}`
- The purpose is to find max w values (and then min values) in order to obtain `z==0` at the end

# provided input paramers :
addx, addy, div:
```
params = [
    (11, 8, 1),  # z = w+8
    (14, 13, 1), # 
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
```

# Steps
All the following steps use the pattern
```
z = z//{div} if w == z%26+{addx} else 26z//{div} + w+{addy}
```

## W0
addx, addy, div = (11, 8, 1),
z = W0+8

## W1
addx, addy, div = (14, 13, 1),
addx>9 => w != z%26+{addx}
z+=w1+13  = 26 * (W0 + 8) + W1 + 13

## W2
addx, addy, div = (10, 2, 1),
z += W2 + 2 => z = 26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2

## W3
addx, addy, div = (0, 7, 26),
if W3 == (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2)%26 + 0 -> W3 == W2 + 2
    z = (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2) // 26 = (26 * (W0 + 8) + W1 + 13) = z @ W1  ******************
else:
    z = 26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7

## W4
addx, addy, div = (12, 11, 1),
z = 26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11

## W5
addx, addy, div = (12, 4, 1),
z = 26 * (26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11) + W5 + 4

## W6
addx, addy, div = (12, 13, 1),
z = 26 * (26 * (26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11) + W5 + 4) + W6 + 13

## W7
addx, addy, div = (-8, 13, 26),
z%26-8 = W6+13-8 = W6+5
if W7 == W6 + 5
    z = 26 * (26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11) + W5 + 4 = z @ W5  ******************
else
    z = 26 * (26 * (26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11) + W5 + 4) + W6 + 13 + W7 + 13

## W8
addx, addy, div = (-9, 10, 26),
if W8 == W5 + 4 -9 == W5 - 5
    z = 26 * (26 * (26 * (W0 + 8) + W1 + 13) + W2 + 2 + W3 + 7) + W4 + 11 = z @ W4  ******************

## W9
addx, addy, div = (11, 1, 1),
z = 26(z@W8) + W9 + 1

## W10
addx, addy, div = (0, 2, 26),
if W10 == W9+1-0 == W9+1
    z = z@W8 = z@W4

## W11
addx, addy, div = (-5, 14, 26),
if W11 == W4+11-5 == W4+6
    z = z@W3 == z@W1

## W12
addx, addy, div = (-6, 6, 26),
if W12 == W1 + 13 - 6 == W1 +7
    z = z@W0

## W13
addx, addy, div = (-12, 14, 26),
if W13 == W0+8-12 == W0-4
    back to 0 !!!


W3 = W2 + 2
    W3 in (3, 9)
    W2 in (1, 7)
W7 == W6 + 5
    W7 in (6, 9)
    W6 in (1, 4)
W8 == W5 - 5
    W8 in (1, 4)
    W5 in (6, 9)
W10 == W9 + 1
    W10 in (2, 9)
    W9 in (1, 8)
W11 == W4 + 6
    W11 in (7, 9)
    W4 in (1, 3)
W12 == W1 + 7
    W12 in (8, 9)
    W1 in (1, 2)
W13 == W0 - 4
    W13 in (1, 5)
    W0 in (5, 9)

# sorted:
W0 in (5, 9)
W1 in (1, 2)
W2 in (1, 7)
W3 in (3, 9)
W4 in (1, 3)
W5 in (6, 9)
W6 in (1, 4)
W7 in (6, 9)
W8 in (1, 4)
W9 in (1, 8)
W10 in (2, 9)
W11 in (7, 9)
W12 in (8, 9)
W13 in (1, 5)
    
# part 1 : 92793949489995
# Part 2 : 51131616112781
