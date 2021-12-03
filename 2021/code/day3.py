from helper_funcs import read_input_file, parse_input_into_list

aoc_day = 3

def binary_to_decimal(input_binary: str):
    val = 0
    for idx, x in enumerate(input_binary[::-1]):
        val += int(x) * (2**idx)
    return val

class Diagnostic():

    def __init__(self, command_list) -> None:
        self.command_list = command_list
        self.n_digits = len(command_list[0])
        self.n_commands = len(command_list)
        self.sum_digits()
        self.get_gamma_epsilon()

    def sum_digits(self):
        self.digit_sums = [0] * self.n_digits
        for x in range(self.n_digits):
            for y in self.command_list:
               self.digit_sums[x] += int(y[x])

    
    def get_gamma_epsilon(self):
        for measure in ['gamma', 'epsilon']:
            if measure == 'gamma':
                y=''
                for x in self.digit_sums:
                    if x > self.n_commands/2:
                        y += '1'
                    else:
                        y += '0'
                self.gamma_binary = y
                self.gamma = binary_to_decimal(y)
            elif measure == 'epsilon':
                y=''
                for x in self.digit_sums:
                    if x > self.n_commands/2:
                        y += '0'
                    else:
                        y += '1'
                self.epsilon_binary = y
                self.epsilon = binary_to_decimal(y)
        self.epsilon_gamma_product = self.epsilon * self.gamma
    

class ComplexDiagnostic():
    def __init__(self, command_list) -> None:
        self.command_list = command_list
        self.n_digits = len(command_list[0])
        self.n_commands = len(command_list)
        self.process_oxygen()
        self.process_co2()
        self.oxygen_co2_product = self.oxygen * self.co2

    def sum_digit(self, idx, command_list):
        digit_sum = 0
        for y in command_list:
            digit_sum += int(y[idx])
        return digit_sum

    def process_oxygen(self):
        tmp_command_list = self.command_list.copy()
        val_to_keep = '1'
        digit = 0
        while True:
            if len(tmp_command_list) == 1:
                self.oxygen_binary = tmp_command_list[0]
                self.oxygen = binary_to_decimal(tmp_command_list[0])
                break
            
            val_to_keep = '1'
            this_digit_sum = self.sum_digit(digit, tmp_command_list)
            if this_digit_sum < len(tmp_command_list)/2:
                val_to_keep = '0'

            new_command_list =[]
            for x in tmp_command_list:
                if x[digit] == val_to_keep:
                    new_command_list.append(x)
            tmp_command_list = new_command_list.copy()
            digit += 1

    def process_co2(self):
        tmp_command_list = self.command_list.copy()
        val_to_keep = '1'
        digit = 0
        while True:
            if len(tmp_command_list) == 1:
                self.co2_binary = tmp_command_list[0]
                self.co2 = binary_to_decimal(tmp_command_list[0])
                break
            
            val_to_keep = '0'
            this_digit_sum = self.sum_digit(digit, tmp_command_list)
            if this_digit_sum < len(tmp_command_list)/2:
                val_to_keep = '1'

            new_command_list =[]
            for x in tmp_command_list:
                if x[digit] == val_to_keep:
                    new_command_list.append(x)
            tmp_command_list = new_command_list.copy()
            digit += 1


def main():
    # Tests

    test_string = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
    '''
    test_list = parse_input_into_list(test_string)

    test_diag = Diagnostic(test_list)
    assert test_diag.gamma == 22
    assert test_diag.epsilon == 9
    assert test_diag.epsilon_gamma_product == 198
    test_diag = ComplexDiagnostic(test_list)
    assert test_diag.oxygen == 23
    assert test_diag.co2 == 10
    assert test_diag.oxygen_co2_product == 230

    # Real Thing

    real_list = parse_input_into_list(read_input_file(f'day{aoc_day}_input.txt'), True)

    real_diag = Diagnostic(real_list)
    real_complex_diag = ComplexDiagnostic(real_list)
    print(f"Step 1: {real_diag.epsilon_gamma_product}")
    print(f"Step 2: {real_complex_diag.oxygen_co2_product}")

if __name__ == '__main__':
    main()