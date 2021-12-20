# target area: x=70..96, y=-179..-124
# x1,x2,y1,y2 = map(int, re.findall(r'-?\d+', input()))

x_min = 70
x_max = 96
y_min = -179
y_max = -124

def reach_target(x_velocity, y_velocity):
    x = y = 0
    x_v, y_v = x_velocity, y_velocity
    step = 0
    while y >= y_min and x <= x_max:
        step += 1
        y += y_v
        x += x_v
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True, step
        x_v = max(0, x_v-1)
        y_v -= 1
    return False, None

ok = []
for x_velocity in range(0, x_max+1):
    for y_velocity in range(y_min, abs(y_min)):
        reached, steps = reach_target(x_velocity, y_velocity)
        if reached:
            ok.append((x_velocity, y_velocity))

print(len(ok))

# 2555
