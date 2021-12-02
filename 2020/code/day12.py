from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 12

def turn_ship(start_compass, direction, degrees):
    turn_list = ['N', 'E', 'S', 'W']
    if direction == 'L':
        turn_list = turn_list[::-1]
    elif direction != 'R':
        raise ValueError

    init_idx = 0
    for idx, d in enumerate(turn_list):
        if start_compass == d:
            init_idx = idx

    turn_spots = int(degrees/90)
    new_idx = turn_spots + init_idx
    while new_idx > 3:
        new_idx = new_idx - 4

    new_heading = turn_list[new_idx]
    return new_heading


def rotate_waypoint(start_pos_ns_ew, direction, degrees):
    quadrant = 0
    new_pos_ns_ew = [0, 0]
    if start_pos_ns_ew[0] >= 0 and start_pos_ns_ew[1] >= 0:
        quadrant = 1
    elif start_pos_ns_ew[0] <= 0 and start_pos_ns_ew[1] <= 0:
        quadrant = 3
    elif start_pos_ns_ew[0] > 0:
        quadrant = 2
    else:
        quadrant = 4
    if degrees > 180:
        degrees = degrees - 180
        if direction == 'L':
            direction = 'R'
        else:
            direction = 'L'

    if degrees == 180:
        new_pos_ns_ew[0] = -start_pos_ns_ew[0]
        new_pos_ns_ew[1] = -start_pos_ns_ew[1]
    elif degrees == 0:
        pass
    elif degrees == 90 and direction == 'R':
        new_pos_ns_ew[0] = -start_pos_ns_ew[1]
        new_pos_ns_ew[1] = start_pos_ns_ew[0]
    elif degrees == 90 and direction == 'L':
        new_pos_ns_ew[0] = start_pos_ns_ew[1]
        new_pos_ns_ew[1] = -start_pos_ns_ew[0]
    return new_pos_ns_ew


def translate_ship(init_position, heading, move_direction, spaces):
    new_position = init_position
    axis = 0
    if move_direction == 'F':
        move_direction = heading
    if move_direction in ['S', 'W']:
        spaces = -1 * spaces
    if move_direction in ['E', 'W']:
        axis = 1

    new_position[axis] = new_position[axis] + spaces

    return new_position

def process_moves(move_list, initial_heading='E', initial_position_ns_ew=None):
    if initial_position_ns_ew is None:
        position_ns_ew = [0, 0]
    else:
        position_ns_ew = initial_position_ns_ew
    heading = initial_heading

    for move in move_list:
        if move[0] in ['L', 'R']:
            heading = turn_ship(heading, move[0], int(move[1:]))
        elif move[0] in ['N', 'E', 'S', 'W', 'F']:
            position_ns_ew = translate_ship(position_ns_ew, heading, move[0], int(move[1:]))

    return position_ns_ew



def process_moves_part2(move_list, initial_waypoint_postion_ns_ew, initial_ship_position_ns_ew):
    ship_position_ns_ew = initial_ship_position_ns_ew
    waypoint_postion_ns_ew = initial_waypoint_postion_ns_ew

    for move in move_list:
        if move[0] in ['L', 'R']:
            waypoint_postion_ns_ew = rotate_waypoint(waypoint_postion_ns_ew, move[0], int(move[1:]))
        elif move[0] in ['N', 'E', 'S', 'W']:
            waypoint_postion_ns_ew = translate_ship(waypoint_postion_ns_ew, 'Q', move[0], int(move[1:]))
        elif move[0] == 'F':
            #Do two moves, one toward each position of waypoint
            north_movement = waypoint_postion_ns_ew[0] * int(move[1:])
            ship_position_ns_ew = translate_ship(ship_position_ns_ew, 'N', 'N', north_movement)

            east_movement = waypoint_postion_ns_ew[1] * int(move[1:])
            ship_position_ns_ew = translate_ship(ship_position_ns_ew, 'N', 'E', east_movement)

    return ship_position_ns_ew

def manhattan_distance(position_ns_ew):
    return abs(position_ns_ew[0]) + abs(position_ns_ew[1])


def main():
    # Tests

    test_string = '''F10
N3
F7
R90
F11
    '''
    test_list = parse_input_into_list(test_string)

    assert (manhattan_distance(process_moves(test_list))) == 25

    assert (manhattan_distance(process_moves_part2(test_list, [1, 10], [0, 0]))) == 286

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)

    print(f'Part 1: Manhattan Distance is {manhattan_distance(process_moves(real_list))}')
    print(f'Part 1: Manhattan Distance is {manhattan_distance(process_moves_part2(real_list, [1, 10], [0, 0]))}')

if __name__ == '__main__':
    main()