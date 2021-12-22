p1_init = 6
p2_init = 10

def roll_dice(dice):
    dice += 1
    if dice > 100:
        dice = 1
    return dice

def move(init_pos, add):
    pos = (init_pos + add) % 10
    if pos == 0:
        pos = 10
    return pos

pos = [p1_init, p2_init]
score =[0, 0]
dice = 0
i = 0
rolls = 0
while score[0] < 1000 and score[1] < 1000:
    dice = roll_dice(dice)
    pos[i] = move(pos[i], dice)
    print(f'dice={dice} -> pos[{i}]={pos[i]}')

    dice = roll_dice(dice)
    pos[i] = move(pos[i], dice)
    print(f'dice={dice} -> pos[{i}]={pos[i]}')

    dice = roll_dice(dice)
    pos[i] = move(pos[i], dice)
    print(f'dice={dice} -> pos[{i}]={pos[i]}')

    score[i] += pos[i]
    print(f'----------------- score[{i}]={score[i]}')

    # dice += 3
    rolls += 3
    print(f'rolls={rolls}')
    i = int(not i)

print(rolls*(score[0] if score[0] < 1000 else score[1]))

# 853776
