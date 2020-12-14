from helper_funcs import read_input_file, parse_input_into_list
import itertools

aoc_day = 14


def int_to_36_bit_binary(n):
    unpadded_binary = [int(x) for x in list('{0:0b}'.format(n))]
    padded_binary = []
    if len(unpadded_binary) < 36:
        for i in range(0, 36 - len(unpadded_binary)):
            padded_binary.append(0)
        for i in unpadded_binary:
            padded_binary.append(i)
    else:
        padded_binary = unpadded_binary
    return padded_binary


def apply_mask_to_binary(mask, binary_list):
    for idx, val in enumerate(mask):
        if val == 'X':
            continue
        else:
            binary_list[idx] = int(val)

    return binary_list

def apply_decode_mask_to_binary(mask, binary_list):
    list_of_xes = []
    set_of_indices = set([])
    for idx, val in enumerate(mask):
        if val == 'X':
            list_of_xes.append(idx)
        elif val == '0':
            continue
        else:
            binary_list[idx] = int(val)
    set_of_indices.add(binary_list_of_ints_to_int(binary_list))
    base_list = binary_list.copy()
    for idx, val in enumerate(base_list):
        if idx in list_of_xes:
            base_list[idx] = 0

    base_number = binary_list_of_ints_to_int(base_list)
    sums_to_add = []
    for x in list_of_xes:
        exponent = len(binary_list) - x - 1
        sums_to_add.append(2**exponent)
    for L in range(0, len(sums_to_add) + 1):
        for subset in itertools.combinations(sums_to_add, L):
            tmp_add = 0
            for n_add in subset:
                tmp_add += n_add
            set_of_indices.add(tmp_add + base_number)

    return set_of_indices

def string_binary_to_list_of_ints(binary_string):
    list_of_ints = []
    for i in binary_string:
        list_of_ints.append(int(i))
    return  list_of_ints

def binary_list_of_ints_to_int(binary_list):
    sum = 0
    for i in range(0,len(binary_list)):
        exponent = len(binary_list) - i - 1
        sum += 2**exponent * binary_list[i]
    return sum

def process_program(list_of_commands):
    init_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mask = init_mask
    memory_registry = {}
    for command in list_of_commands:
        if command[1] == 'a': # mask
            mask = command.split(' ')[-1]
        else: # setting address value
            idx = command.split(' =')[0]
            idx = idx[4:]
            idx = idx[:-1]

            value = int(command.split(' = ')[1])
            value_bin = int_to_36_bit_binary(value)
            value_masked = apply_mask_to_binary(mask, value_bin)
            value = binary_list_of_ints_to_int(value_masked)
            memory_registry[idx] = value
    return memory_registry

def process_program_v2(list_of_commands):
    init_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mask = init_mask
    memory_registry = {}
    for command in list_of_commands:
        if command[1] == 'a': # mask
            mask = command.split(' ')[-1]
        else: # setting address value
            idx = command.split(' =')[0]
            idx = idx[4:]
            idx = int(idx[:-1])

            value = int(command.split(' = ')[1])
            idx_bin = int_to_36_bit_binary(idx)
            idx_list = apply_decode_mask_to_binary(mask, idx_bin)
            for i in idx_list:
                memory_registry[i] = value
    return memory_registry

def sum_nonzero_registries(memory_registry):
    sum = 0
    for key in memory_registry.keys():
        if memory_registry[key] != 0:
            sum += memory_registry[key]
    return sum

def main():
    # Tests

    test_string = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
    '''
    test_list = parse_input_into_list(test_string)

    assert len(int_to_36_bit_binary(24)) == 36
    assert apply_mask_to_binary(
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        int_to_36_bit_binary(101)) == string_binary_to_list_of_ints('000000000000000000000000000001100101')
    assert binary_list_of_ints_to_int(string_binary_to_list_of_ints('000000000000000000000000000001100101')) == 101

    assert sum_nonzero_registries(process_program(test_list)) == 165

    test_string_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

    assert binary_list_of_ints_to_int(string_binary_to_list_of_ints('000000000000000000000000000000101010')) == 42
    test_list_2 = parse_input_into_list(test_string_2)
    assert sum_nonzero_registries((process_program_v2(test_list_2))) == 208

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)

    print(f'Part 1: Sum of non-zero registry entries is: {sum_nonzero_registries(process_program(real_list))}')
    print(f'Part 2: Sum of non-zero registry entries is: {sum_nonzero_registries(process_program_v2(real_list))}')

if __name__ == '__main__':
    main()