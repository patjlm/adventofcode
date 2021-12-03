with open('day1.input', 'r') as f:
  a = [int(i) for i in f.read().strip().split('\n')]

count = 0
for i in range(3, len(a)):
  # comparing a[i-3]+a[i-2]+a[i-1] and a[i-2]+a[i-1]+a[i] is 
  # the same as comparing a[i-3] and a[i]
  if a[i] > a[i-3]:
    count += 1

print(count)
# 1633
