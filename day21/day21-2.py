import functools

p1_init = 6
p2_init = 10

goal = 21

# each possible 3-rolls value and its probability
rolls_values = [z + y + x for x in range(1,4)
                          for y in range(1,4)
                          for z in range(1,4)]
rolls = {a:rolls_values.count(a) for a in rolls_values}

# each possible game state, with each possible score. There are 44100 of these...
states={(p1_position, p2_position, p1_score, p2_score): 0
            for p1_position in range(1, 11)
            for p2_position in range(1, 11)
            for p1_score in range(0, goal)
            for p2_score in range(0, goal)}
states[(p1_init, p2_init, 0, 0)] = 1

@functools.lru_cache
def move(pos_init, roll):
    return (pos_init + roll - 1) % 10 + 1

victories = [0, 0]

while not max(states.values()) == 0:
    for state, count in states.items():
        p1_pos, p2_pos, p1_score, p2_score = state
        if count == 0:
            continue
        for p1_roll, p1_roll_factor in rolls.items():
            for p2_roll, p2_roll_factor in rolls.items():
                pos = [move(p1_pos, p1_roll), move(p2_pos, p2_roll)]
                new_scores = [p1_score + pos[0], p2_score + pos[1]]
                if max(new_scores) < goal:  # neither player wins
                    states[tuple(pos + new_scores)] += count * p1_roll_factor * p2_roll_factor
                elif new_scores[1] >= goal and new_scores[0] < goal:  # player 2 wins
                    victories[1] += count * p2_roll_factor * p1_roll_factor
            if new_scores[0] >= goal:  # player 1 wins before player 2 played
                victories[0] += count * p1_roll_factor
        states[state] = 0  # resetting the previous state

print(max([victories[0], victories[1]]))

# 301304993766094
