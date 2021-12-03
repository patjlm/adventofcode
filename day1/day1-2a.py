with open('day1.input', 'r') as f:
  a = [int(i) for i in f.read().strip().split('\n')]

count = 0
previous = a[0] + a[1] + a[2]
for i in range(3, len(a)):
  cur = a[i-2] + a[i-1] + a[i]
  if cur > previous:
    count += 1
  previous = cur

print(count)
# 1633
