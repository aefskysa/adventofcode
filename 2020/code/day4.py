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


def validate_passport(passport_dict, needed_fields=[], strict=False, validation_dict={}):
    return_val = True
    for field in needed_fields:
        if field not in passport_dict and field != 'cid':
            return False
        if strict:
            valid_tuple = validation_dict[field]
            if len(valid_tuple) == 0:
                return_val = return_val and True
            if len(valid_tuple) == 1:
                return_val = return_val and valid_tuple[0](passport_dict[field])
            if len(valid_tuple) == 2:
                return_val = return_val and valid_tuple[0](passport_dict[field], valid_tuple[1])
            if len(valid_tuple) == 4:
                return_val = return_val and valid_tuple[0](passport_dict[field], valid_tuple[1], valid_tuple[2], valid_tuple[3])
        if not return_val:
            return False
    return return_val


def validate_number_string_field(test_val, length, min=None, max=None):
    if len(test_val) != length:
        return False
    try:
        int_val = int(test_val)
    except:
        return False
    if min is not None and max is not None:
        if int_val < min or int_val > max:
            return False
    return True

def validate_hair(test_val):
    if len(test_val) != 7:
        return False
    if test_val[0] != '#':
        return False
    for idx in range(1,7):
        if test_val[idx] not in '0123456789abcdef':
            return False
    return True

def validate_eye(test_val):
    return test_val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_height(test_val):
    unit = test_val[-2:]
    if unit not in ['cm', 'in']:
        return False
    val = test_val[:-2]
    try:
        int_val = int(val)
    except:
        return False
    if unit == 'cm':
        return int_val >= 150 and int_val <= 193
    else:
        return int_val >=59 and int_val <=76


def count_valid_passports(passports_dict, needed_fields=[], strict=False, validation_dict={}):
    count = 0
    for key in passports_dict.keys():
        if validate_passport(passports_dict[key], needed_fields, strict, validation_dict):
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

    validation_dict = {'byr': (validate_number_string_field, 4, 1920, 2002),
                       'iyr': (validate_number_string_field, 4, 2010, 2020),
                       'eyr': (validate_number_string_field, 4, 2020, 2030),
                       'hgt': [validate_height],
                       'hcl': [validate_hair],
                       'ecl': [validate_eye],
                       'pid': (validate_number_string_field, 9),
                       'cid': ()}

    assert validation_dict['byr'][0]('2002', validation_dict['byr'][1], validation_dict['byr'][2], validation_dict['byr'][3]) is True
    assert validation_dict['byr'][0]('2003', validation_dict['byr'][1], validation_dict['byr'][2], validation_dict['byr'][3]) is False

    assert validation_dict['hgt'][0]('60in') is True
    assert validation_dict['hgt'][0]('190cm') is True
    assert validation_dict['hgt'][0]('190in') is False
    assert validation_dict['hgt'][0]('190') is False

    assert validation_dict['hcl'][0]('#123abc') is True
    assert validation_dict['hcl'][0]('#123abz') is False
    assert validation_dict['hcl'][0]('123abc') is False

    assert validation_dict['ecl'][0]('brn') is True
    assert validation_dict['ecl'][0]('wat') is False

    assert validation_dict['pid'][0]('000000001', validation_dict['pid'][1]) is True
    assert validation_dict['pid'][0]('0123456789', validation_dict['pid'][1]) is False

    bad_test_passports = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

    bad_passport_records = [r for r in bad_test_passports.split('\n')]
    bad_passport_dict = parse_passport_dict_from_list(bad_passport_records)

    assert count_valid_passports(bad_passport_dict, needed_fields, True, validation_dict) == 0

    good_test_passports = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''
    good_passport_records = [r for r in good_test_passports.split('\n')]
    good_passport_dict = parse_passport_dict_from_list(good_passport_records)
    assert count_valid_passports(good_passport_dict, needed_fields, True, validation_dict) == 4

    print(f'Part 2: {count_valid_passports(passport_dict, needed_fields, True, validation_dict)} Valid Passports')


if __name__ == "__main__":
    main()