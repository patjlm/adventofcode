with open('input.txt', 'r') as f:
    line = f.read().strip()

positions = list(map(int, line.split(',')))

min_pos = min(positions)
max_pos = max(positions)
min_fuel = -1
target = None
targets = [0]*(max_pos - min_pos + 1)
a=0
for i in range(min_pos, max_pos):
    fuel = 0
    for p in positions:
        n = abs(p-i)
        # 1+2+3+...+n = n(n+1)/2. and that's always an int.
        fuel += int(n*(n+1)/2)
        if i==2:
            print(f'{p} target {i}: +{int(n*(n+1)/2)} = {fuel}')
    if i==2:
        print(f'target {i}: fuel = {fuel}')
    if fuel < min_fuel or min_fuel == -1:
        target = i
        min_fuel = fuel
    targets[a] = fuel
    a+=1

# print(targets)

print(f'fuel {min_fuel} for target position {target}')

# fuel 91638945 for target position 466
# 91638945
