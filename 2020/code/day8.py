from helper_funcs import read_input_file, parse_input_into_list


def parse_code_into_tuples(command_list):
    code_order = []
    for line in command_list:
        command = line.split(' ')[0]
        value = line.split(' ')[1]
        code_order.append([command, int(value)])
    return code_order


def find_broken_line(code_tuples):
    for idx, line in enumerate(code_tuples):
        reached_end = False
        accumulator = 0
        if line[0] == 'acc':
            continue
        if line[0] == 'nop':
            code_tuples[idx][0] = 'jmp'
            accumulator, reached_end = step_through_code(code_tuples)
            code_tuples[idx][0] = 'nop'
        if line[0] == 'jmp':
            code_tuples[idx][0] = 'nop'
            accumulator, reached_end = step_through_code(code_tuples)
            code_tuples[idx][0] = 'jmp'

        if reached_end:
            return idx, accumulator



def step_through_code(code_tuples):
    commands_already_run = set([])
    n_commands_run = 0
    current_line = 0
    accumulator = 0
    reached_end = False
    while True:
        commands_already_run.add(current_line)
        if n_commands_run + 1 != len(commands_already_run) or reached_end:
            break
        if current_line == len(code_tuples) - 1:
            reached_end = True
        this_line = code_tuples[current_line]
        if this_line[0] == 'nop':
            current_line = current_line + 1
        elif this_line[0] == 'acc':
            current_line = current_line + 1
            accumulator = accumulator + this_line[1]
        elif this_line[0] == 'jmp':
            current_line = current_line + this_line[1]

        n_commands_run = n_commands_run + 1
    return accumulator, reached_end

def main():

    # Tests
    test_code = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6    
    '''
    test_command_list = parse_input_into_list(test_code)
    test_command_tuples = parse_code_into_tuples(test_command_list)

    assert step_through_code(test_command_tuples)[0] == 5

    assert find_broken_line(test_command_tuples) == (7, 8)

    # Real Thing
    all_commands_list = parse_input_into_list(read_input_file('day8_input.txt'), True)
    all_command_tuples = parse_code_into_tuples(all_commands_list)

    print(f'Part 1: Before repeated line, accumulator is {step_through_code(all_command_tuples)[0]}')
    bad_line, accumulator = find_broken_line(all_command_tuples)
    print(f'Part 2: After fixing line {bad_line}, accumulator is {accumulator}')

if __name__ == "__main__":
    main()