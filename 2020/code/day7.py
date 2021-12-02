from helper_funcs import read_input_file, parse_input_into_list


def parse_individual_rule(rule_string):
    outer = rule_string.split('contain')[0]
    outer = outer[:-6]

    modifier = outer.split(' ')[0]
    color = outer.split(' ')[1]
    bag_rule_dict = {}
    bag_rule_dict['outer'] = {'modifier': modifier, 'color': color}

    inner = rule_string.split('contain')[1].strip()
    if inner.strip() == 'no other bags.':
        inner = []
        bag_rule_dict['inner'] = inner
    else:
        list_of_bags = inner.split(',')
        inner_list_of_bags = []
        for bag_def in list_of_bags:
            tmp_bag_def = bag_def.strip()
            quantity = int(tmp_bag_def.split(' ')[0])
            modifier = tmp_bag_def.split(' ')[1]
            color = tmp_bag_def.split(' ')[2]
            inner_list_of_bags.append({'quantity': quantity, 'modifier': modifier, 'color': color})
        bag_rule_dict['inner'] = inner_list_of_bags

    return bag_rule_dict


def get_outer_bags(bag_of_interest_modifier, bag_of_interest_color, bag_rules, set_of_colors=None):
    if set_of_colors is None:
        set_of_colors = set([])
    for rule in bag_rules:
        for inner_bag in rule['inner']:
            if inner_bag['modifier'] == bag_of_interest_modifier and inner_bag['color'] == bag_of_interest_color:
                set_of_colors.add(rule['outer']['modifier'] + rule['outer']['color'])
                set_of_colors = set_of_colors.union(get_outer_bags(rule['outer']['modifier'], rule['outer']['color'], bag_rules, set_of_colors))
    return set_of_colors


def count_inner_bags(bag_of_interest_modifier, bag_of_interest_color, bag_rules, count_of_bags=0):

    for rule in bag_rules:
        outer_bag = rule['outer']
        if outer_bag['modifier'] == bag_of_interest_modifier and outer_bag['color'] == bag_of_interest_color:
            if len(rule['inner']) == 0:
                return 0
            for inner_bag in rule['inner']:
                n_inner = inner_bag['quantity']
                count_of_bags = count_of_bags + n_inner + n_inner*count_inner_bags(inner_bag['modifier'], inner_bag['color'], bag_rules)
    return count_of_bags


def main():

    # Tests

    test_rules = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
    '''
    test_rules_list = parse_input_into_list(test_rules)

    test_bag_rules = []
    for i in test_rules_list:
        test_bag_rules.append(parse_individual_rule(i))

    test_set = set([])
    assert len(get_outer_bags('shiny', 'gold', test_bag_rules)) == 4

    assert count_inner_bags('dotted', 'black', test_bag_rules) == 0
    assert count_inner_bags('vibrant', 'plum', test_bag_rules) == 11

    assert count_inner_bags('shiny', 'gold', test_bag_rules) == 32

    test_rules_2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
    '''
    test_rules_list = parse_input_into_list(test_rules_2)

    test_bag_rules = []
    for i in test_rules_list:
        test_bag_rules.append(parse_individual_rule(i))

    assert count_inner_bags('shiny', 'gold', test_bag_rules) == 126

    # Real Thing
    all_bag_rules_list = parse_input_into_list(read_input_file('day7_input.txt'), True)
    all_bag_rules = []
    for i in all_bag_rules_list:
        all_bag_rules.append(parse_individual_rule(i))


    outer_bags = get_outer_bags('shiny', 'gold', all_bag_rules)
    print(f"Part 1: Shiny Gold Bag can be in {len(outer_bags)} distinct other bags")
    inner_bags = count_inner_bags('shiny', 'gold', all_bag_rules)
    print(f"Part 1: Shiny Gold Bag has {inner_bags} bags inside it")


if __name__ == "__main__":
    main()