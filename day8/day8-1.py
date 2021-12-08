def parse():
    with open('input.txt', 'r') as f:
        for line in f:
            yield line.strip().split(' | ')[1].split()

count = 0
for patterns in parse():
    for pattern in patterns:
        if len(pattern) in [2, 3, 4, 7]:
            count += 1

print(count)

# 479
