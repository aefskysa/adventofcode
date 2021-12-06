from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 6

def create_fish_state(input_list, max_life=9):
    init_days = [int(x) for x in input_list[0].split(',')]
    each_day_count = [0] * (max_life + 1) # Positions in this list correspond to -1 to 8 for part1
    for d in init_days:
        for c in range(len(each_day_count)):
            if d == c-1:
                each_day_count[c] += 1
    return each_day_count

def evolve_fish(fish_state, ndays, regen_idx=7):
    for d in range(ndays + 1):
        new_state = fish_state.copy()
        new_fish = 0
        regen_fish = 0
        if d == 0:
            continue
        for idx, c in enumerate(fish_state):
            new_state[idx-1] = c
        new_state[regen_idx] += new_state[0]
        new_state[-1] = new_state[0]
        fish_state = new_state
    return fish_state

def count_fish(fish_state):
    return sum(fish_state[1:])
        


def main():
    # Tests

    test_string = '''3,4,3,1,2'''
    test_list = parse_input_into_list(test_string)

    fish_state = create_fish_state(test_list)
    assert count_fish(evolve_fish(fish_state, 2)) == 6
    assert count_fish(evolve_fish(fish_state, 18)) == 26
    assert count_fish(evolve_fish(fish_state, 80)) == 5934
    assert count_fish(evolve_fish(fish_state, 256)) == 26984457539

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    fish_state = create_fish_state(real_list)
    print(f"Step 1: {count_fish(evolve_fish(fish_state, 80))}")
    print(f"Step 2: {count_fish(evolve_fish(fish_state, 256))}")

if __name__ == '__main__':
    main()