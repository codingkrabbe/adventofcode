if __name__ == '__main__':
    # init
    count_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma_rate_str = ''
    epsilon_rate_str = ''

    with open('03-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    for row in text_input:
        row = row.replace('\n', '')
        for idx_row, char in enumerate(row):
            if char == '1':
                count_ones[idx_row] += 1
            else:
                count_zeroes[idx_row] += 1

    for i in range(12):  # check gamma rate
        if count_ones[i] > count_zeroes[i]:
            gamma_rate_str += '1'
            epsilon_rate_str += '0'
        else:
            gamma_rate_str += '0'
            epsilon_rate_str += '1'
    result = int(gamma_rate_str, 2) * int(epsilon_rate_str, 2)
    print(result)
