with open('input.txt', 'r') as f:
    input_line = f.readline().strip()

inputs = list(map(int, input_line.split(',')))

count = [0]*9
# for i in range(9):
#     count[i] = inputs.count(i)
for i in inputs:
    count[i] += 1

for day in range(256):
    spawned = count[0]
    for i in range(6):
        count[i] = count[i+1]
    count[6] = count[7] + spawned
    count[7] = count[8]
    count[8] = spawned

print(count)
print(sum(count))

# 1738377086345
