from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 4

class BingoCard():
    def __init__(self, card_array) -> None:
        card_rows = []
        marked_rows = []
        for row in card_array:
            card_rows.append([int(x) for x in row.strip().replace('  ', ' ').split(' ')])
            marked_rows.append([0]*5)
        self.card_array = card_rows
        self.marked_card = marked_rows
        self.bingo = False
        self.sum_unmarked = None
    
    def check_bingo(self):
        for row in self.marked_card:
            if sum(row) == 5:
                self.bingo = True
                return True

        for col in range(5):
            this_col = [x[col] for x in self.marked_card]
            if sum(this_col) == 5:
                self.bingo = True
                return True

    def mark_number(self, called_number):
        for row_idx, row in enumerate(self.card_array):
            for col, x in enumerate(row):
                if called_number == x:
                    self.marked_card[row_idx][col] = 1
    
    def sum_unmarked_bingo(self):
        if self.sum_unmarked:
            return self.sum_unmarked
        this_sum = 0
        for row_idx, row in enumerate(self.marked_card):
            for col, x in enumerate(row):
                if self.marked_card[row_idx][col] == 0:
                    this_sum += self.card_array[row_idx][col]
        self.sum_unmarked = this_sum
        return this_sum

def process_bingo(cards, called_numbers, first_win=True):

    results_dict = {}
    bingo = False
    cards_with_bingo = []
    for n in called_numbers:
        for idx, c in enumerate(cards):
            if idx in cards_with_bingo:
                continue
            c.mark_number(n)
            if c.check_bingo():
                results_dict['last_draw'] = n
                results_dict['winning_card_sum_unmarked'] = c.sum_unmarked_bingo()
                results_dict['winning_card_index'] = idx
                results_dict['winning_card_product'] = n * c.sum_unmarked_bingo()
                bingo = True
                cards_with_bingo.append(idx)
                if first_win:
                    break
        if bingo:
            if first_win:
                break
    return results_dict


def process_bingo_cards(input_list):
    card_start_indices=[]
    list_of_cards = []
    called_numbers = [int(x) for x in input_list[0].split(',')]
    for idx, line in enumerate(input_list):
        if idx == 0:
            continue
        if line == '':
            card_start_indices.append(idx+1)
    
    for idx in card_start_indices:
        this_card = BingoCard(input_list[idx:idx+5])
        list_of_cards.append(this_card)
    return called_numbers, list_of_cards

def main():
    # Tests

    test_string = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
    '''
    test_list = parse_input_into_list(test_string, ignore_blank_rows=False)
    called_numbers, cards = process_bingo_cards(test_list)
    test_results_first_win = process_bingo(cards, called_numbers)
    assert test_results_first_win['last_draw'] == 24
    assert test_results_first_win['winning_card_index'] == 2
    assert test_results_first_win['winning_card_sum_unmarked'] == 188
    assert test_results_first_win['winning_card_product'] == 4512
    
    test_results_last_win = process_bingo(cards, called_numbers, False)
    assert test_results_last_win['last_draw'] == 13
    assert test_results_last_win['winning_card_index'] == 1
    assert test_results_last_win['winning_card_sum_unmarked'] == 148
    assert test_results_last_win['winning_card_product'] == 1924

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), False)
    called_numbers, cards = process_bingo_cards(real_list)
    real_results_first_win = process_bingo(cards, called_numbers)
    real_results_last_win = process_bingo(cards, called_numbers, False)

    print(f"Step 1: {real_results_first_win['winning_card_product']}")
    print(f"Step 2: {real_results_last_win['winning_card_product']}")

if __name__ == '__main__':
    main()