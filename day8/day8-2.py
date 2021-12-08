def parse():
    with open('/Users/patmarti/dev/adventofcode/day8/input.txt', 'r') as f:
        for line in f:
            yield line.strip().split(' | ')

segments = {}
sum=0
for signal_patterns, output_digits in parse():
    patterns = sorted(signal_patterns.split(), key=len)
    inputs = [set(p) for p in patterns]

    # find patterns for 1, 7, 4 and 8
    segments[1] = inputs[0]
    segments[7] = inputs[1]
    segments[4] = inputs[2]
    segments[8] = inputs[9]

    # find patterns for 9, 6, 0 which have 6 segments each
    for input in [inputs[6], inputs[7], inputs[8]]:
        if len(input & segments[4]) == 4:
            segments[9] = input
        elif len(input & segments[1]) == 1:
            segments[6] = input
        else:
            segments[0] = input

    # find patterns for 3, 5, 2 which have 5 segments each
    for input in [inputs[3], inputs[4], inputs[5]]:
        if len(input & segments[1]) == 2:
            segments[3] = input
        elif len(input - segments[9]) == 0:
            segments[5] = input
        else:
            segments[2] = input

    # sorts the characters of a string
    sort = lambda s: ''.join(sorted(s))

    # digit for each (sorted) pattern
    digits = {sort(v): k for k, v in segments.items()}

    # list of (sorted) output patterns
    outputs = list(map(sort, output_digits.split()))

    out = digits[outputs[0]] * 1000 + \
          digits[outputs[1]] * 100 + \
          digits[outputs[2]] * 10 + \
          digits[outputs[3]]
    sum += out

print(sum)

# 1041746
