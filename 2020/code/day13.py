from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 13

def get_bus_cadences1(sched_string):
    init_cadences = sched_string.split(',')
    final_cadences = []
    for c in init_cadences:
        if c == 'x':
            continue
        else:
            final_cadences.append(int(c))
    return final_cadences

def get_bus_cadences(sched_string):
    init_cadences = sched_string.split(',')
    final_cadences = []
    for idx, c in enumerate(init_cadences):
        if c == 'x':
            continue
        else:
            final_cadences.append((int(c), idx))
    return final_cadences


def find_earliest_bus(sched_list):
    earliest_depart = int(sched_list[0])
    cadences = get_bus_cadences1(sched_list[1])

    max_iterations = 1 + earliest_depart // min(cadences)
    min_delta = 1e6
    final_bus_id = None
    for bus_id in cadences:
        for j in range(0, max_iterations):
            if j * bus_id < earliest_depart:
                continue
            else:
                if j*bus_id - earliest_depart < min_delta:
                    min_delta = j*bus_id - earliest_depart
                    final_bus_id = bus_id
                break
    return final_bus_id, min_delta


def find_earliest_consecutive_buses(cadences, init_val=0, iterator=1):
    a = init_val
    first_bus_cadence = cadences[0][0]
    while True:
        reached_end = True
        for c in cadences[1:]:
            val = (a * first_bus_cadence + c[1])/c[0]
            if not val.is_integer():
                reached_end = False
                break

        if reached_end:
            if a != 13087 :
                break
        a = a + iterator
    return a, a*first_bus_cadence

def find_earliest_consecutive_buses_long(cadences):
    next_iterator = 1
    first_bus_cadence = cadences[0][0]
    init_val = 0
    for idx, c in enumerate(cadences):
        if idx == 0:
            continue
        a, b = find_earliest_consecutive_buses(cadences[0:idx+1], init_val, next_iterator)
        init_val = a
        next_iterator = 1
        for c in cadences[1:idx]:
            next_iterator *= c[0]
    return init_val * first_bus_cadence

def main():
    # Tests

    test_string = '''939
7,13,x,x,59,x,31,19
    '''
    test_list = parse_input_into_list(test_string)

    test_bus_id, test_min_delta = find_earliest_bus(test_list)
    assert test_bus_id * test_min_delta == 295

    assert find_earliest_consecutive_buses(get_bus_cadences(test_list[1]))[1] == 1068781
    assert find_earliest_consecutive_buses(get_bus_cadences('17,x,13,19'))[1] == 3417
    assert find_earliest_consecutive_buses_long(get_bus_cadences('17,x,13,19')) == 3417
    assert find_earliest_consecutive_buses_long(get_bus_cadences('67,7,59,61')) == 754018
    assert find_earliest_consecutive_buses_long(get_bus_cadences('67,x,7,59,61')) == 779210
    assert find_earliest_consecutive_buses_long(get_bus_cadences('67,7,x,59,61')) == 1261476
    assert find_earliest_consecutive_buses_long(get_bus_cadences('1789,37,47,1889')) == 1202161486


    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    part1_bus_id, part_1_min_delta = find_earliest_bus(real_list)



    print(f'Part 1: Bus ID is {part1_bus_id}, Arrives {part_1_min_delta} after earliest departure. Product is {part1_bus_id * part_1_min_delta}')
    print(f'Part 2: First Time With Consecutive Buses is {find_earliest_consecutive_buses_long(get_bus_cadences(real_list[1]))}')


if __name__ == '__main__':
    main()