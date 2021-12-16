from dataclasses import dataclass

weights = []
with open('/Users/patmarti/dev/adventofcode/day15/input.txt', 'r') as f:
  for line in f:
    weights.append(list(map(int, line.strip())))

rows = len(weights)
cols = len(weights[0])


@dataclass
class Node():
  weight: int
  row: int
  col: int
  distance: int = float('inf')

  # compare both the distance and the weight
  def __lt__(self, other):
    return (self.distance, self.weight) < (other.distance, other.weight)

  def __ge__(self, other):
    return not self.__lt__(other)


data = [ [ Node(weights[row][col], row, col) for col in range(cols) ] for row in range(rows) ]
data[0][0] = Node(0, 0, 0, distance=0)

def adjacents(data, node):
  row, col = node.row, node.col
  return [data[r][c]
          for r, c in ((row-1, col), (row, col-1), (row+1, col), (row, col+1))
          if r >= 0 and c >= 0 and r < rows and c < cols]

def inspect(visiting, adj: Node, dist):
    adj.distance = dist
    # insert this node in the visiting list according to its distance (shortest distance last)
    if not visiting or adj < visiting[-1]:
        visiting += [adj]
        return
    for i in range(len(visiting)):
        if adj >= visiting[i]:
            visiting.insert(i, adj)
            return

visiting = [data[0][0]]
# visit nodes starting by closest ones (visiting is ordered by descending distance)
while visiting and (node := visiting.pop()):
  dist = node.distance + node.weight
  for adj in adjacents(data, node):
    if adj.distance > dist:
      inspect(visiting, adj, dist)

target = data[rows-1][cols-1]
print(target.distance + target.weight)

# 423
