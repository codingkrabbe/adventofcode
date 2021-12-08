def get_mapping_1(digits):
    for digit in digits:
        if len(digit) == 2:
            return set(digit)


def get_mapping_4(digits):
    for digit in digits:
        if len(digit) == 4:
            return set(digit)


def get_mapping_7(digits):
    for digit in digits:
        if len(digit) == 3:
            return set(digit)


def get_mapping_8(digits):
    for digit in digits:
        if len(digit) == 7:
            return set(digit)


def get_mapping_9(digits, mappings):
    for digit in digits:
        if len(digit) == 6 and mappings[4].issubset(set(digit)):
            return set(digit)


def get_mapping_0(digits, mappings):
    for digit in digits:
        if len(digit) == 6 and mappings[1].issubset(set(digit)):
            return set(digit)


def get_mapping_6(digits, mappings):
    for digit in digits:
        if len(digit) == 6:
            return set(digit)


def get_mapping_5(digits, mappings):
    for digit in digits:
        if len(digit) == 5 and set(digit).issubset(mappings[6]):
            return set(digit)


def get_mapping_3(digits, mappings):
    for digit in digits:
        if len(digit) == 5 and set(digit).issubset(mappings[9]):
            return set(digit)


def get_mapping_2(digits, mappings):
    for digit in digits:
        if len(digit) == 5:
            return set(digit)


def remove_identified_digits(digits, digit_sets):
    output_digits = digits.copy()
    for digit in digits:
        if set(digit) in digit_sets:
            output_digits.remove(digit)
    return output_digits


def get_output_number(digits, output):
    output_str = ''
    if len(digits) == 10 and len(output) == 4:
        digit_sets = [set()] * 10

        # ez
        digit_sets[1] = get_mapping_1(digits)
        digit_sets[4] = get_mapping_4(digits)
        digit_sets[7] = get_mapping_7(digits)
        digit_sets[8] = get_mapping_8(digits)
        digits = remove_identified_digits(digits, digit_sets)

        # 6 wires
        digit_sets[9] = get_mapping_9(digits, digit_sets)
        digits = remove_identified_digits(digits, digit_sets)
        digit_sets[0] = get_mapping_0(digits, digit_sets)
        digits = remove_identified_digits(digits, digit_sets)
        digit_sets[6] = get_mapping_6(digits, digit_sets)
        digits = remove_identified_digits(digits, digit_sets)

        # 5 wires
        digit_sets[5] = get_mapping_5(digits, digit_sets)
        digits = remove_identified_digits(digits, digit_sets)
        digit_sets[3] = get_mapping_3(digits, digit_sets)
        digits = remove_identified_digits(digits, digit_sets)
        digit_sets[2] = get_mapping_2(digits, digit_sets)

        for output_digit in output:
            output_str = output_str + str(digit_sets.index(set(output_digit)))
        return int(output_str)


def main():
    lines = open('input.txt', 'r').readlines()
    sum = 0
    for line in lines:
        digits, output = line.split(' | ')
        output_number = get_output_number(digits.split(), output.split())
        sum += output_number
    print('Sum of outputs: ' + str(sum))


if __name__ == '__main__':
    main()
