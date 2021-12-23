from functools import lru_cache

rooms = (("C", "B"), ("B", "D"), ("D", "A"), ("A", "C"))

room_pos = (2, 4, 6, 8)
hall_places = (0, 1, 3, 5, 7, 9, 10)
target_room = {"A": 0, "B": 1, "C": 2, "D": 3}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

hallway = tuple(None for _ in range(len(room_pos) + len(hall_places)))

def can_reach_in_hallway(fro, to, hallway):
    return all([hallway[pos] is None for pos in range(min(to, fro), max(to, fro)+1)])

def can_enter_room(abcd, room):
    for other in room:
            if other is not None and other != abcd:  # Foreigner in room: can't move there.
                return False
    return True


@lru_cache(maxsize=None)
def get_best_cost(hallway, rooms):
    if rooms == (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")):
        return 0

    best_cost = float('inf')
    for pos, abcd in enumerate(hallway):  # Move from the hallway into a room.
        if abcd is None:
            continue
        dest = target_room[abcd]
        if not can_enter_room(abcd, rooms[dest]):
            continue
        offset = 1 if room_pos[dest] > pos else -1
        if not can_reach_in_hallway(pos + offset, room_pos[dest], hallway):
            continue
        none_count = sum(elem is None for elem in rooms[dest])
        new_room = (None,) * (none_count - 1) + (abcd,) * (2 - none_count + 1)
        steps = none_count + abs(pos - room_pos[dest])
        cost = steps * costs[abcd]
        sub_cost = get_best_cost(hallway[:pos] + (None,) + hallway[pos + 1:],
                               rooms[:dest] + (new_room,) + rooms[dest + 1:])
        new_cost = cost + sub_cost
        if new_cost < best_cost:
            best_cost = new_cost
    for room_id, room in enumerate(rooms):  # Move from a room into the hallway.
        needs_exit = False
        for elem in room:
            if elem is not None and target_room[elem] != room_id:
                needs_exit = True
        if not needs_exit:
            continue
        none_count = sum(elem is None for elem in room)
        exit_steps = none_count + 1
        abcd = room[none_count]
        for hall_destination in hall_places:
            steps = exit_steps + abs(hall_destination - room_pos[room_id])
            cost = steps * costs[abcd]
            if not can_reach_in_hallway(room_pos[room_id], hall_destination, hallway):
                continue
            new_room = (None,) * (none_count + 1) + room[none_count + 1:]
            sub_cost = get_best_cost(
                hallway[:hall_destination] + (abcd,) + hallway[hall_destination + 1:],
                rooms[:room_id] + (new_room,) + rooms[room_id + 1:])
            new_cost = cost + sub_cost
            if new_cost < best_cost:
                best_cost = new_cost
    return best_cost

cost = get_best_cost(hallway, rooms)
print(cost)

 # 13520    
