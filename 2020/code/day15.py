from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 15


class NumberGame(object):
    def __init__(self):
        self.nturns = 2020
        self.numbers_last_spot = {}
        self.counter = 0
        self.last_number = 0

    def play_number(self, n):

        if n not in self.numbers_last_spot.keys():
            last_occurrence = self.counter
        else:
            last_occurrence = self.numbers_last_spot[n]
        time_since_last = self.counter - last_occurrence
        self.numbers_last_spot[n] = self.counter
        self.counter += 1
        return time_since_last

    def play_game(self, starting_numbers):
        for idx, i in enumerate(starting_numbers):
            if idx < len(starting_numbers) - 1:
                self.numbers_last_spot[i] = idx + 1
            self.last_number = i
            self.counter += 1
        n_turns_left = self.nturns - len(starting_numbers)
        for i in range(0, n_turns_left):
            next_number = self.play_number(self.last_number)
            self.last_number = next_number

    def get_last_number(self):
        return self.last_number

    def reset_list(self):
        self.numbers_last_spot = {}
        self.counter = 0
        self.last_number = 0


def main():
    # Tests
    test_game = NumberGame()

    # test_game.nturns = 10
    test_game.play_game([0,3,6])
    assert test_game.get_last_number() == 436
    test_game.reset_list()

    test_game.play_game([1,3,2])
    assert test_game.get_last_number() == 1
    test_game.reset_list()

    test_game.play_game([2,1,3])
    assert test_game.get_last_number() == 10
    test_game.reset_list()

    test_game.play_game([1,2,3])
    assert test_game.get_last_number() == 27
    test_game.reset_list()

    test_game.play_game([2,3,1])
    assert test_game.get_last_number() == 78
    test_game.reset_list()

    test_game.play_game([3,2,1])
    assert test_game.get_last_number() == 438
    test_game.reset_list()

    test_game.play_game([3,1,2])
    assert test_game.get_last_number() == 1836
    test_game.reset_list()

    # Part 2 Tests
    # test_game.nturns = 30000000
    # test_game.play_game([0,3,6])
    # assert test_game.get_last_number() == 175594
    # test_game.reset_list()
    #
    # test_game.play_game([1,3,2])
    # assert test_game.get_last_number() == 2578
    # test_game.reset_list()
    #
    # test_game.play_game([2,1,3])
    # assert test_game.get_last_number() == 3544142
    # test_game.reset_list()
    #
    # test_game.play_game([1,2,3])
    # assert test_game.get_last_number() == 261214
    # test_game.reset_list()
    #
    # test_game.play_game([2,3,1])
    # assert test_game.get_last_number() == 6895259
    # test_game.reset_list()
    #
    # test_game.play_game([3,2,1])
    # assert test_game.get_last_number() == 18
    # test_game.reset_list()
    #
    # test_game.play_game([3,1,2])
    # assert test_game.get_last_number() == 362
    # test_game.reset_list()


    # Real Thing
    game_part1 = NumberGame()
    game_part1.play_game([14,3,1,0,9,5])
    print(f'Part 1: 2020th number played is {game_part1.get_last_number()}')

    game_part2 = NumberGame()
    game_part2.nturns = 30000000
    game_part2.play_game([14,3,1,0,9,5])
    print(f'Part 2: 30000000 number played is {game_part2.get_last_number()}')

if __name__ == '__main__':
    main()