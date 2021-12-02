from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 2

def process_moves(inputs, init_pos=None):
    moves = [(x.split()[0], int(x.split()[1])) for x in inputs]
    pos = [0,0] if not init_pos else init_pos
    for move in moves:
        # print(move)
        if move[0] == 'forward':
            pos[0] += move[1]
        elif move[0] == 'up':
            pos[1] -= move[1]
        elif move[0] == 'down':
            pos[1] += move[1]
    result_dict = {'horiz': pos[0], 'depth': pos[1], 'product': pos[0]*pos[1]}
    return result_dict

def process_moves_with_aim(inputs, init_pos=None):
    moves = [(x.split()[0], int(x.split()[1])) for x in inputs]
    pos = [0,0] if not init_pos else init_pos
    aim = 0
    for move in moves:
        # print(move)
        if move[0] == 'forward':
            pos[0] += move[1]
            pos[1] += aim * move[1] 
        elif move[0] == 'up':
            aim -= move[1]
        elif move[0] == 'down':
            aim += move[1]
    result_dict = {'horiz': pos[0], 'depth': pos[1], 'product': pos[0]*pos[1]}
    return result_dict


def main():
    # Tests

    test_string = '''forward 5
down 5
forward 8
up 3
down 8
forward 2
    '''
    test_list = parse_input_into_list(test_string)

    assert process_moves(test_list)['depth'] == 10
    assert process_moves(test_list)['horiz'] == 15
    assert process_moves(test_list)['product'] == 150
    assert process_moves_with_aim(test_list)['depth'] == 60
    assert process_moves_with_aim(test_list)['horiz'] == 15
    assert process_moves_with_aim(test_list)['product'] == 900

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    result = process_moves(real_list)
    result2 = process_moves_with_aim(real_list)
    print(f"Step 1: {result['product']}")
    print(f"Step 2: {result2['product']}")
    
    

if __name__ == '__main__':
    main()