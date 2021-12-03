with open('day1.input', 'r') as f:
  a = [int(i) for i in f.read().strip().split('\n')]

count = 0
previous = a[0]
for i in a[1:]:
  if i > previous:
    count += 1
  previous = i

print(count)
# 1602
