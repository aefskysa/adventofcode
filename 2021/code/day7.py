from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 7

def fuel_per_step(x: int):
    return sum(range(x+1))

def find_minimum(start_positions, multi_fuel=False):
    pos_array = [int(x) for x in start_positions[0].split(',')]
    min_fuel = 1e9
    for x in range(min(pos_array), max(pos_array)):
        fuel_calc = []
        for p in pos_array:
            if multi_fuel:
                fuel_calc.append(fuel_per_step(abs(p-x)))
            else:
                fuel_calc.append(abs(p-x))
        if sum(fuel_calc) < min_fuel:
            min_fuel = sum(fuel_calc)
    return min_fuel

def main():
    # Tests

    test_string = '''16,1,2,0,4,2,7,1,2,14
    '''
    test_list = parse_input_into_list(test_string)
    assert find_minimum(test_list) == 37
    assert find_minimum(test_list, True) == 168

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    print(f"Step 1: {find_minimum(real_list)}")
    print(f"Step 2: {find_minimum(real_list, True)}")

if __name__ == '__main__':
    main()