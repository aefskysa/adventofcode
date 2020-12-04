def parse_passport_dict_from_list(row_list):
    dict_of_dicts = {}
    passport_index = 0
    tmp_dict = {}
    for idx, row in enumerate(row_list):
        if idx == len(row_list) - 1:
            continue
        if row == '':
            dict_of_dicts[passport_index] = tmp_dict
            tmp_dict = {}
            passport_index = passport_index + 1
            continue
        key_vals = row.split(' ')
        for pair in key_vals:
            tmp_dict[pair.split(':')[0]] = pair.split(':')[1]
    dict_of_dicts[passport_index] = tmp_dict

    return dict_of_dicts


def validate_passport(passport_dict, needed_fields=[]):
    for field in needed_fields:
        if field not in passport_dict:
            return False
    return True


def count_valid_passports(passports_dict, needed_fields=[]):
    count = 0
    for key in passports_dict.keys():
        if validate_passport(passports_dict[key], needed_fields):
            count = count + 1
    return count

def main():

    test_input = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
    '''
    passport_test_records = [r for r in test_input.split('\n')]
    test_passport_dict = parse_passport_dict_from_list(passport_test_records)

    needed_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    assert validate_passport(test_passport_dict[0], needed_fields) is True
    assert validate_passport(test_passport_dict[1], needed_fields) is False
    assert validate_passport(test_passport_dict[2], needed_fields) is True
    assert validate_passport(test_passport_dict[3], needed_fields) is False
    assert count_valid_passports(test_passport_dict, needed_fields) == 2

    with open('../inputs/day4_input.txt', 'r') as f:
        file_string = f.read()

    passport_records = [r for r in file_string.split('\n')]
    passport_dict = parse_passport_dict_from_list(passport_records)

    print(f'Part 1: {count_valid_passports(passport_dict, needed_fields)} Valid Passports')


if __name__ == "__main__":
    main()