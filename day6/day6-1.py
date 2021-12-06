with open('input.txt', 'r') as f:
    input_line = f.readline().strip()

inputs = list(map(int, input_line.split(',')))

count = [0]*9
# not using this as we'd traverse inputs 9 times instead of 1
# for i in range(9):
#     count[i] = inputs.count(i)
for i in inputs:
    count[i] += 1

for day in range(80):
    spawned = count[0]
    for i in range(8):
        count[i] = count[i+1]
    count[6] += spawned  # parents reset
    count[8] = spawned  # new borns

print(sum(count))

# 387413
