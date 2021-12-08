def count_1478(digits, output):
    sum = 0
    if len(digits) == 10 and len(output) == 4:
        digit_sets = [set()] * 10
        for digit in digits:
            if len(digit) == 2:
                digit_sets[1] = set(digit)
            elif len(digit) == 3:
                digit_sets[7] = set(digit)
            elif len(digit) == 4:
                digit_sets[4] = set(digit)
            elif len(digit) == 7:
                digit_sets[8] = set(digit)
        for output_digit in output:
            if set(output_digit) in digit_sets:
                sum += 1
        return sum


def main():
    lines = open('input.txt', 'r').readlines()
    sum_1478 = 0
    for line in lines:
        digits, output = line.split(' | ')
        sum_1478 += count_1478(digits.split(), output.split())
    print('Number of 1s, 4s, 7s and 8s in output: ' + str(sum_1478))


if __name__ == '__main__':
    main()
