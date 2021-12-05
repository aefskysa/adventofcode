from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 5

def mark_map_from_lines(input_lines, include_45s=False):

    starts = []
    ends = []
    for line in input_lines:
        start_pt = [int(x) for x in line.split(' ')[0].split(',')]
        end_pt = [int(x) for x in line.split(' ')[-1].split(',')]
        starts.append(start_pt)
        ends.append(end_pt)
    
    # Need to get max dimensons in order to build square grid
    max_x = 0
    max_y = 0
    for x in starts:
        if x[0] > max_x:
            max_x = x[0]
        if x[1] > max_y:
            max_y = x[1]
    for x in ends:
        if x[0] > max_x:
            max_x = x[0]
        if x[1] > max_y:
            max_y = x[1]

    map_rows = []
    for r in range(max_x+1):
        this_row = []
        for c in range(max_y+1):
            this_row.append(0)
        map_rows.append(this_row)
    
    # Mark the map

    points_to_mark = []
    for idx, this_start in enumerate(starts):
        is_bad_diag = False
        this_end = ends[idx]
        is_45 = (abs(this_start[0] - this_end[0]) == abs(this_start[1] - this_end[1]))
        if this_start[0] != this_end[0] and this_start[1] != this_end[1] and not is_45:
            is_bad_diag = True

        if is_bad_diag or (is_45 and not include_45s):
            continue

        if this_start[0] == this_end[0]:
            if this_start[1] > this_end[1]:
                tmp_idx = this_end[1]
                while tmp_idx <= this_start[1]:
                    points_to_mark.append([this_start[0], tmp_idx])
                    tmp_idx += 1
            if this_start[1] < this_end[1]:
                tmp_idx = this_start[1]
                while tmp_idx <= this_end[1]:
                    points_to_mark.append([this_start[0], tmp_idx])
                    tmp_idx += 1
        elif this_start[1] == this_end[1]:
            if this_start[0] > this_end[0]:
                tmp_idx = this_end[0]
                while tmp_idx <= this_start[0]:
                    points_to_mark.append([tmp_idx, this_start[1]])
                    tmp_idx += 1
            if this_start[0] < this_end[0]:
                tmp_idx = this_start[0]
                while tmp_idx <= this_end[0]:
                    points_to_mark.append([tmp_idx, this_start[1]])
                    tmp_idx += 1
        else:
            x_sign = 1 if this_start[0] < this_end[0] else -1
            y_sign = 1 if this_start[1] < this_end[1] else -1
            tmp_point = this_start
            while tmp_point != this_end:
                points_to_mark.append(tmp_point.copy())
                tmp_point[0] += x_sign
                tmp_point[1] += y_sign
            points_to_mark.append(this_end)

        
    for mark_pt in points_to_mark:
        map_rows[mark_pt[0]][mark_pt[1]] += 1

    n_multi_overlap = 0
    for row in map_rows:
        for col in row:
            if col > 1:
                n_multi_overlap += 1
    return n_multi_overlap, map_rows


def main():
    # Tests

    test_string = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
    '''
    test_list = parse_input_into_list(test_string)
    n_multi_overlap, map_rows = mark_map_from_lines(test_list) 
    assert n_multi_overlap == 5
    n_multi_overlap, map_rows = mark_map_from_lines(test_list, True) 
    assert n_multi_overlap == 12
    

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    n_multi_overlap, map_rows = mark_map_from_lines(real_list) 
    n_multi_overlap_with_45s, map_rows = mark_map_from_lines(real_list, True) 
    print(f"Step 1: {n_multi_overlap}")
    print(f"Step 2: {n_multi_overlap_with_45s}")

if __name__ == '__main__':
    main()