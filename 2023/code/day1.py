from helper_funcs import read_input_file, parse_input_into_list
import re

aoc_day = 1

def numbers_from_string(input, text_also=False):
    nums = []
    if text_also:
        return string_replace_nums(input)

    else:
        [nums.append(x) if x.isnumeric() else None for x in input]
    return int(f'{nums[0]}{nums[-1]}')

def sum_parsed_nums_from_list(input, text_also=False):
    running_sum = 0
    for i in input:
        running_sum += numbers_from_string(i, text_also)
    return running_sum

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def string_replace_nums(input):
    replace_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    min_pos = 100
    max_pos = -1
    min_dig = None
    max_dig = None
    for k in replace_dict.keys():
        tmp_pos = find_all(input, k)
        for t in tmp_pos:
            print(k, t)
            if t < min_pos:
                min_pos = t
                min_dig = replace_dict[k]
            if t > max_pos:
                max_pos = t
                max_dig = replace_dict[k]
            print(min_pos, min_dig, max_pos, max_dig)
    print(int(f'{min_dig}{max_dig}'))
    return int(f'{min_dig}{max_dig}')
        

    

def main():
    # Tests

    test_string = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
    '''
    test_list = parse_input_into_list(test_string)

    assert sum_parsed_nums_from_list(test_list) == 142

    test_string2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
    '''
    test_list2 = parse_input_into_list(test_string2)
    assert sum_parsed_nums_from_list(test_list2, True) == 281

    assert numbers_from_string('nine671seventwotwonejkf', True) == 91

    # Real Thing



    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    print(f"Step 1: {sum_parsed_nums_from_list(real_list, False)}")
    print(f"Step 2: {sum_parsed_nums_from_list(real_list, True)}")

if __name__ == '__main__':
    main()
