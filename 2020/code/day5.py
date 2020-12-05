from math import floor, ceil

def binary_partition(val_string, low_key, high_key, low_val, high_val):
    value = val_string[0]
    midpoint = (high_val - low_val)/2 + low_val
    end_state = False
    if len(val_string) > 1:
        new_val_string = val_string[1:]
    else:
        end_state = True
    if value == low_key:
        if end_state:
            return low_val
        else:
            return binary_partition(new_val_string, low_key, high_key, low_val, floor(midpoint))
    if value == high_key:
        if end_state:
            return high_val
        else:
            return binary_partition(new_val_string, low_key, high_key, ceil(midpoint), high_val)


def get_seat(seat_string, nrows=128, ncols=8):
    row_substring = seat_string[:7]
    col_substring = seat_string[-3:]
    row = binary_partition(row_substring, 'F', 'B', 0, 127)
    col = binary_partition(col_substring, 'L', 'R', 0, 7)
    return row, col, row*8 + col


def get_all_seat_ids(list_of_seats):
    seat_ids = []
    for seat in list_of_seats:
        seat_ids.append(get_seat(seat)[2])
    return seat_ids


def get_missing_seat_id(sorted_seat_ids):
    for idx in range(0, len(sorted_seat_ids)):
        if sorted_seat_ids[idx]+1 not in sorted_seat_ids:
            return sorted_seat_ids[idx]+1

def main():

    test_0 = get_seat('FBFBBFFRLR')
    assert test_0[0] == 44
    assert test_0[1] == 5
    assert test_0[2] == 357

    test_1 = get_seat('BFFFBBFRRR')
    assert test_1[0] == 70
    assert test_1[1] == 7
    assert test_1[2] == 567

    test_2 = get_seat('FFFBBBFRRR')
    assert test_2[0] == 14
    assert test_2[1] == 7
    assert test_2[2] == 119

    test_3 = get_seat('BBFFBBFRLL')
    assert test_3[0] == 102
    assert test_3[1] == 4
    assert test_3[2] == 820


    with open('../inputs/day5_input.txt', 'r') as f:
        file_string = f.read()
    seat_records = [r for r in file_string.split('\n') if r.strip()]

    all_seat_ids = get_all_seat_ids(seat_records)
    print(f'Part 1: Max Seat ID is {max(all_seat_ids)}')

    missing_seat = get_missing_seat_id(sorted(all_seat_ids))
    print(f'Part 2: My Seat ID is {missing_seat}')

if __name__ == "__main__":
    main()