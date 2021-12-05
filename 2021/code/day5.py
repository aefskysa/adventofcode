from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 0

def main():
    # Tests

    test_string = '''
    '''
    test_list = parse_input_into_list(test_string)

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    print(f"Step 1: {None}")
    print(f"Step 2: {None}")

if __name__ == '__main__':
    main()