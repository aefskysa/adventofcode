from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 16


class TicketFinder(object):
    def __init__(self, ticket_string):

        self.rules = {}
        self.my_ticket = []
        self.other_tickets = []
        self.ticket_string = ticket_string
        self.bad_tickets = []
        self.rule_final_positions = {}

        self.parse_ticket_details()

    def parse_ticket_details(self):
        section_start = 0
        for idx, line in enumerate(self.ticket_string):
            if line == '':
                section_start = idx
                break
            rule_name = line.split(':')[0]
            ranges = line.split(':')[1].split(' ')
            first_range = ranges[1].split('-')
            second_range = ranges[-1].split('-')
            first_range = [int(first_range[0]), int(first_range[1])]
            second_range = [int(second_range[0]), int(second_range[1])]
            self.rules[rule_name] = [first_range, second_range]

        my_ticket = self.ticket_string[section_start + 2]
        self.my_ticket = [int(x) for x in my_ticket.split(',')]

        for idx in range(section_start + 5, len(self.ticket_string) - 1):
            line = self.ticket_string[idx]
            self.other_tickets.append([int(x) for x in line.split(',')])

    def find_error_rate(self):
        sum_bad_vals = 0
        for idx, ticket in enumerate(self.other_tickets):
            for val in ticket:
                is_good_val = False
                for rule_key in self.rules.keys():
                    is_good_val = self.ticket_val_passes_rule(val, rule_key)
                    if is_good_val:
                        break
                if not is_good_val:
                    sum_bad_vals += val
                    # print(idx)
                    self.bad_tickets.append(idx)
        return sum_bad_vals

    def remove_bad_tickets(self):
        good_tickets = []
        for idx, ticket in enumerate(self.other_tickets):
            if idx in self.bad_tickets:
                continue
            good_tickets.append(ticket)
        self.other_tickets = good_tickets
        self.bad_tickets = []

    def ticket_val_passes_rule(self, val, rule_key, verbose=False):
        this_rule = self.rules[rule_key]
        passes_rule = False
        for this_range in this_rule:
            if verbose:
                print(this_range, val, this_range[0] <= val <= this_range[1])
            if this_range[0] <= val <= this_range[1]:
                passes_rule = True
                break
        return passes_rule

    def determine_rule_positions(self):
        rule_potential_postions = {}
        n_rules = len(self.rules)
        for rule_key in self.rules:
            good_positions = []
            for position, my_val in enumerate(self.my_ticket):
                potential_position = True
                for ticket in self.other_tickets:
                    if not self.ticket_val_passes_rule(ticket[position], rule_key, False):
                        # print(rule_key, position, self.rules[rule_key], ticket[position], ticket)
                        potential_position = False
                        break
                if potential_position:
                    good_positions.append(position)
            rule_potential_postions[rule_key] = good_positions
        # print(rule_potential_postions)

        rule_final_positions = {}
        n_solo = 0
        while True:
            if n_rules == n_solo:
                break
            for rule_key in self.rules:
                if len(rule_potential_postions[rule_key]) == 1:
                    n_solo +=1
                    final_pos = rule_potential_postions[rule_key][0]
                    rule_final_positions[rule_key] = final_pos
                    for inner_rule_key in self.rules:
                        if final_pos in rule_potential_postions[inner_rule_key]:
                            rule_potential_postions[inner_rule_key].remove(final_pos)
        self.rule_final_positions = rule_final_positions

    def product_departure_fields(self):
        product = 1
        for rule_key in self.rules:
            if rule_key[0:9] == 'departure':
                product *= (self.my_ticket[self.rule_final_positions[rule_key]])
        return product


def main():
    # Tests

    test_string = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''
    test_list = parse_input_into_list(test_string, False)
    test_finder = TicketFinder(test_list)
    assert test_finder.find_error_rate() == 71

    test_string = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''
    test_list = parse_input_into_list(test_string, False)
    test_finder = TicketFinder(test_list)
    test_finder.remove_bad_tickets()
    test_finder.determine_rule_positions()

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), False)
    finder = TicketFinder(real_list)

    print(f'Part 1: Total sum of errors is: {finder.find_error_rate()}')
    finder.remove_bad_tickets()
    finder.determine_rule_positions()
    print(f'Part 2: Product of Departure Fields is: {finder.product_departure_fields()}')

if __name__ == '__main__':
    main()