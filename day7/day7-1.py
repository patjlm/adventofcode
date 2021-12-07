with open('input.txt', 'r') as f:
    line = f.read().strip()

positions = list(map(int, line.split(',')))

min_pos = min(positions)
max_pos = max(positions)
min_fuel = None
target = None
for i in range(min_pos, max_pos):
    fuel = 0
    for p in positions:
        fuel += abs(p-i)
    if i==2:
        print(f'target {i}: fuel = {fuel}')
    if min_fuel is None or fuel < min_fuel:
        target = i
        min_fuel = fuel

print(f'fuel {min_fuel} for target position {target}')

# fuel 336721 for target position 316
# 336721
