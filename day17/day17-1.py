# target area: x=70..96, y=-179..-124
# x1,x2,y1,y2 = map(int, re.findall(r'-?\d+', input()))

x_min = 70
x_max = 96
y_min = -179
y_max = -124

# x & y velovity is independant, let's concentrate only on y for part 1

def top_height(y_velocity):
    y = 0
    velocity = y_velocity
    max_h = y_min
    step = 0
    while y >= y_min:
        step += 1
        y += velocity
        max_h = max(max_h, y)
        if y_min <= y <= y_max:
            return max_h
        velocity -= 1
    return None

max_height ={}
for y_velocity in range(y_min, abs(y_min)):
    h = top_height(y_velocity)
    if h:
        max_height[y_velocity] = h

print(max_height[max(max_height, key=lambda v: max_height[v])])

# 15931
