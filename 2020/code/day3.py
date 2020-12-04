def traverse_trees(list_of_rows, x, y):
    mod_value = len(list_of_rows[0])

    x_test = 0
    y_test = 0
    count_trees = 0
    while y_test < len(list_of_rows):
        new_spot = list_of_rows[y_test][x_test % mod_value]
        if new_spot == '#':
            count_trees = count_trees + 1
        x_test = x_test + x
        y_test = y_test + y

    return count_trees


def main():

    with open('../inputs/day3_input.txt', 'r') as f:
        file_string = f.read()

    records = [r for r in file_string.split('\n') if r.strip()]


    test_input1 = '''
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    '''
    test_records = [r.strip() for r in test_input1.split('\n') if r.strip()]

    assert traverse_trees(test_records, x=3, y=1) == 7

    n_trees = traverse_trees(records, 3, 1)

    slope_tuples = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    end_product_test = 1
    end_product = 1
    for tuple in slope_tuples:
        end_product_test = end_product_test * (traverse_trees(test_records, x=tuple[0], y=tuple[1]))
        end_product = end_product * (traverse_trees(records, x=tuple[0], y=tuple[1]))

    assert  end_product_test == 336

    print(f'Step 1: {n_trees} Trees Hit')
    print(f'Step 2: {end_product} Product of Trees Hit')
    return

if __name__ == "__main__":
    main()