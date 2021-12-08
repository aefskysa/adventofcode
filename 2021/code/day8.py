from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 8

digit_segment_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

default_values = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def parse_notes(input_list):
    seen_patterns = []
    output_values = []
    for l in input_list:
        seen_patterns.append([set(x) for x in l.split('|')[0].split(' ')[:-1]])
        output_values.append([''.join(x) for x in l.split('|')[1].split(' ')[1:]])
    return seen_patterns, output_values

def count_easy(output_values):
    count = 0
    for l in output_values:
        for v in l:
            if len(v) in [2,4,3,7]:
                count +=1
    return count

def build_map_from_patterns(seen_patterns):

    map_dict = {}

    # Patterns which correspond to 1 and 7 lock in the 'a', others are 'c' or 'f'
    for x in seen_patterns:
        if len(x) == 2:
            p_one = x
        elif len(x) == 3:
            p_seven = x
        elif len(x) == 4:
            p_four = x
    
    map_dict['a'] = [x for x in p_seven.difference(p_one)][0]

    # b Shows up 6 times, f 9 times, e 4 times; these counts are unique
    letter_count_dict = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
    for x in seen_patterns: 
        for l in x:
            letter_count_dict[l] += 1
    
    d_g_candidates = []
    for key, val in letter_count_dict.items():
        if val == 6:
            map_dict['b'] = key
        if val == 9:
            map_dict['f'] = key
        if val == 4:
            map_dict['e'] = key
        if val == 7:
            d_g_candidates.append(key)
    
    # Whichever segment is in one that is not the 'f' must be 'c'
    map_dict['c'] = [x for x in p_one.difference({map_dict['f']})][0]
    
    # d shows up in the pattern for 4, g does not
    for v in d_g_candidates:
        if v in p_four:
            map_dict['d'] = v
        else:
            map_dict['g'] = v

    # Want the dict reversed
    return {val: key for key,val in map_dict.items()}

def process_line(seen_patterns, output_values):
    map_dict = build_map_from_patterns(seen_patterns)
    int_vals = []
    for v in output_values:
        true_string = sorted(''.join([map_dict[x] for x in v]))
        int_vals.append(default_values[(''.join(true_string))])
    value = 1000*int_vals[0] + 100*int_vals[1] + 10*int_vals[2] + int_vals[3]
    return value

def process_all(seen_patterns, output_values):
    sum_val = 0
    for idx, sp in enumerate(seen_patterns):
        sum_val += process_line(sp, output_values[idx])
    return sum_val


def main():
    # Tests

    test_string = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
    '''
    test_list = parse_input_into_list(test_string)
    seen_patterns, output_values = (parse_notes(test_list))
    assert count_easy(output_values) == 26
    assert process_all(seen_patterns, output_values) == 61229

    process_line(seen_patterns[0], output_values[0])

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)
    seen_patterns, output_values = (parse_notes(real_list))
    print(f"Step 1: {count_easy(output_values)}")
    print(f"Step 2: {process_all(seen_patterns, output_values)}")

if __name__ == '__main__':
    main()