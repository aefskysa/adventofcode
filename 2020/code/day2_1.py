import csv

def check_password_step1(line: str):
    password = line.split(':')[1].strip()
    rule = line.split(':')[0]
    rule_letter = rule.split(' ')[1]
    rule_min = int(rule.split(' ')[0].split('-')[0])
    rule_max = int(rule.split(' ')[0].split('-')[1])

    n_appearance = password.count(rule_letter)
    if rule_min <= n_appearance <= rule_max:
        return True
    else:
        return False


def check_password_step2(line: str):
    password = line.split(':')[1].strip()
    rule = line.split(':')[0]
    rule_letter = rule.split(' ')[1]
    rule_first_pos = int(rule.split(' ')[0].split('-')[0]) - 1
    rule_second_pos = int(rule.split(' ')[0].split('-')[1]) - 1

    first_pos_check = password[rule_first_pos] == rule_letter

    second_pos_check = password[rule_second_pos] == rule_letter
    return first_pos_check ^ second_pos_check # This is xor in Python



def main():
    list_obj = []
    with open('../inputs/day2_1_input.txt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_obj.append(row[0])

    test_input1 = '1-3 a: abcde'
    test_input2 = '1-3 b: cdefg'
    test_input3 = '2-9 c: ccccccccc'

    assert check_password_step1(test_input1) is True
    assert check_password_step1(test_input2) is False
    assert check_password_step1(test_input3) is True


    assert check_password_step2(test_input1) is True
    assert check_password_step2(test_input2) is False
    assert check_password_step2(test_input3) is False

    n_valid_pw_1 = 0
    n_valid_pw_2 = 0
    for row in list_obj:
        a = check_password_step1(row)
        if a:
            n_valid_pw_1 = n_valid_pw_1 + 1
        a = check_password_step2(row)
        if a:
            n_valid_pw_2 = n_valid_pw_2 + 1

    print(f'Step 1: {n_valid_pw_1} Valid Passwords')
    print(f'Step 2: {n_valid_pw_2} Valid Passwords')
    return

if __name__ == "__main__":
    main()