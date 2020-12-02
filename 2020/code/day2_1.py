
def parse_line(line: str):
    password = line.split(':')[1].strip()
    rule = line.split(':')[0]
    rule_letter = rule.split(' ')[1]
    rule_min = int(rule.split(' ')[0].split('-')[0])
    rule_max = int(rule.split(' ')[0].split('-')[1])

    return password, rule, rule_letter, rule_min, rule_max

def check_password_step1(line: str):

    password, rule, rule_letter, rule_min, rule_max = parse_line(line)

    n_appearance = password.count(rule_letter)
    if rule_min <= n_appearance <= rule_max:
        return True
    else:
        return False


def check_password_step2(line: str):

    password, rule, rule_letter, rule_first_pos, rule_second_pos = parse_line(line)
    rule_first_pos = rule_first_pos - 1
    rule_second_pos = rule_second_pos - 1

    first_pos_check = password[rule_first_pos] == rule_letter

    second_pos_check = password[rule_second_pos] == rule_letter
    return first_pos_check ^ second_pos_check # This is xor in Python



def main():

    with open('../inputs/day2_1_input.txt', 'r') as f:
        file_string = f.read()

    records = [r for r in file_string.split('\n') if r.strip()]


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
    for row in records:
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