from helper_funcs import read_input_file, parse_input_into_list


def sum_of_group_yeses(group_responses, union=True):

    sum_groups = 0
    for group in group_responses:
        sum_groups = sum_groups + count_yeses(group, union)

    return sum_groups


def count_yeses(list_of_responses, union=True):
    if union:
        final_set = set()
    else:
        final_set = set('qwertyuiopasdfghjklzxcvbnm')
    for single_response in list_of_responses:
        uniques = set(single_response)
        if union:
            final_set = final_set.union(uniques)
        else:
            final_set = final_set.intersection(uniques)

    return len(final_set)


def separate_input_into_groups(all_responses):
    list_of_lists = []
    tmp_list = []
    for idx, row in enumerate(all_responses):
        if idx == len(all_responses) - 1:
            continue
        if row == '':
            list_of_lists.append(tmp_list)
            tmp_list = []
            continue
        tmp_list.append(row)
    list_of_lists.append(tmp_list)

    return list_of_lists


def main():

    # Tests
    test_input_single = '''abcx
abcy
abcz
    '''
    test_input_single_list = parse_input_into_list(test_input_single)
    assert count_yeses(test_input_single_list) == 6


    test_input_multiple = '''abc

a
b
c

ab
ac

a
a
a
a

b
    '''

    test_input_multiple_list = parse_input_into_list(test_input_multiple, ignore_blank_rows=False)
    test_group_responses = separate_input_into_groups(test_input_multiple_list)

    assert count_yeses(test_group_responses[0]) == 3
    assert count_yeses(test_group_responses[1]) == 3
    assert count_yeses(test_group_responses[2]) == 3
    assert count_yeses(test_group_responses[3]) == 1
    assert count_yeses(test_group_responses[4]) == 1

    assert sum_of_group_yeses(test_group_responses) == 11

    assert count_yeses(test_group_responses[0], False) == 3
    assert count_yeses(test_group_responses[1], False) == 0
    assert count_yeses(test_group_responses[2], False) == 1
    assert count_yeses(test_group_responses[3], False) == 1
    assert count_yeses(test_group_responses[4], False) == 1
    assert sum_of_group_yeses(test_group_responses, False) == 6

    # Real thing
    group_response_list = parse_input_into_list(read_input_file('day6_input.txt'), False)
    group_responses = separate_input_into_groups(group_response_list)

    print(f'Part 1: Sum of Unique Yeses is {sum_of_group_yeses(group_responses)}')
    print(f'Part 2: Sum of Intersected Yeses is {sum_of_group_yeses(group_responses, False)}')




if __name__ == "__main__":
    main()