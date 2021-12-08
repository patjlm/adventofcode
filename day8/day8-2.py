def parse():
    with open('/Users/patmarti/dev/adventofcode/day8/input.txt', 'r') as f:
        for line in f:
            yield line.strip().split(' | ')

segments = {}
sum=0
for signal_patterns, output_digits in parse():
    patterns = sorted(signal_patterns.split(), key=len)
    s = [set(p) for p in patterns]

    segments[1] = s[0]
    segments[7] = s[1]
    segments[4] = s[2]
    segments[8] = s[9]

    for segs in [s[6], s[7], s[8]]:  # len = 6
        if len(segs & segments[4]) == 4:
            segments[9] = segs
        elif len(segs & segments[1]) == 1:
            segments[6] = segs
        else:
            segments[0] = segs

    for segs in [s[3], s[4], s[5]]:  # len = 5
        if len(segs & segments[1]) == 2:
            segments[3] = segs
        elif len(segs - segments[9]) == 0:
            segments[5] = segs
        else:
            segments[2] = segs

    revert = {''.join(sorted(v)): k for k, v in segments.items()}

    outputs = list(map(lambda s: ''.join(sorted(s)), output_digits.split()))
    out = revert[outputs[0]] * 1000 + \
          revert[outputs[1]] * 100 + \
          revert[outputs[2]] * 10 + \
          revert[outputs[3]]
    sum += out

print(sum)

# 1041746
