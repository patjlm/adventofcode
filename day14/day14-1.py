from dataclasses import dataclass

pairs = {}
with open('/Users/patmarti/dev/adventofcode/day14/input.txt', 'r') as f:
    template = f.readline().strip()
    for line in f:
        if line.strip():
            a, b = line.strip().split(' -> ')
            pairs[tuple(a)] = b

@dataclass
class Node():
    letter: str
    next = None

first = Node(template[0])
node = first
for l in template[1:]:
    n = Node(l)
    node.next = n
    node = n

def iter_node_letters():
    node = first
    yield first.letter
    while node.next:
        node = node.next
        yield node.letter

for step in range(10):
    node = first
    while node.next:
        if (node.letter, node.next.letter) in pairs:
            n = Node(pairs[(node.letter, node.next.letter)])
            n.next = node.next
            node.next = n
        node = n.next

counts = {}
node = first
while node:
    counts.setdefault(node.letter, 0)
    counts[node.letter] += 1
    node = node.next

min_count = min(counts.values())
max_count = max(counts.values())

# print(counts)
# print(f'min={min_count}, max={max_count}')
print(max_count - min_count)

# 3143
