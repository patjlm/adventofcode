from collections import defaultdict

insert = {}
with open('/Users/patmarti/dev/adventofcode/day14/input.txt', 'r') as f:
    template = f.readline().strip()
    for line in f:
        if line.strip():
            a, b = line.strip().split(' -> ')
            insert[tuple(a)] = b

letters = defaultdict(int)
pair_count = defaultdict(int)

for i in range(len(template) - 1):
    letters[template[i]] += 1
    pair_count[(template[i], template[i+1])] += 1
letters[template[-1]] += 1

for i in range(40):
    for pair, count in pair_count.copy().items():
        pair_count[pair] -= count
        add = insert[pair]
        pair_count[(pair[0], add)] += count
        pair_count[(add, pair[1])] += count
        letters[add] += count
    
print(max(letters.values()) - min(letters.values()))

# 4110215602456
