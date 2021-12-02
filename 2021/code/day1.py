from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 1

def count_single_increases(input):
    count = 0
    input = [int(i) for i in input]
    for idx, x in enumerate(input):
        if idx == 0:
            continue
        if input[idx] > input[idx-1]:
            count = count + 1
    return count

def count_windows_increases(input):
    count = 0
    input = [int(i) for i in input]
    for idx, x in enumerate(input):
        if idx < 3 or idx > len(input) - 1:
            continue
        this_sum = sum(input[idx-3:idx])
        next_sum = sum(input[idx-2:idx+1])
        if next_sum > this_sum:
            count = count + 1
    return count

def main():
    # Tests

    test_string = '''
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    '''
    test_list = parse_input_into_list(test_string)

    assert count_single_increases(test_list) == 7
    assert count_windows_increases(test_list) == 5

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    step1_count = count_single_increases(real_list)
    step2_count = count_windows_increases(real_list)
    print(f'Step 1: {step1_count} Single Step Increases')
    print(f'Step 2: {step2_count} Window Increases')


if __name__ == '__main__':
    main()