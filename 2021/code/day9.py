from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 9

def parse_grid(grid_str_list):
    rows = []
    for row in grid_str_list:
        this_row = [int(x) for x in row]
        rows.append(this_row)
    return rows

def brute_force_low_points(grid):
    x_len = len(grid[0])
    y_len = len(grid)
    low_count = 0
    risk_level = 0

    print(x_len, y_len)

    for test_x in range(x_len):
        for test_y in range(y_len):
            this_val = grid[test_y][test_x]
            is_low = True
            for x_move in [-1,1]:
                if (test_x + x_move < 0 or test_x + x_move > x_len - 1):
                    continue
                elif not is_low:
                    continue
                else:
                    check_pt = grid[test_y][test_x + x_move]
                    if check_pt <= this_val:
                        is_low = False
            for y_move in [-1,1]:
                if (test_y + y_move < 0 or test_y + y_move > y_len - 1):
                    continue
                elif not is_low:
                    continue
                else:
                    check_pt = grid[test_y + y_move][test_x]
                    if check_pt <= this_val:
                        is_low = False
            if is_low:
                # print(this_val, test_y, test_x)
                low_count += 1
                risk_level += (this_val + 1)
    return low_count, risk_level


def main():
    # Tests

    test_string = '''2199943210
3987894921
9856789892
8767896789
9899965678
    '''
    test_list = parse_input_into_list(test_string)
    test_grid = parse_grid(test_list)
    test_res = brute_force_low_points(test_grid)

    assert test_res[0] == 4
    assert test_res[1] == 15

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    real_grid = parse_grid(real_list)
    real_res = brute_force_low_points(real_grid)
    print(f"Step 1: {real_res[1]}")
    print(f"Step 2: {None}")

if __name__ == '__main__':
    main()