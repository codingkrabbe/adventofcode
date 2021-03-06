if __name__ == '__main__':
    # init
    count_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open('03-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()

    oxygen = text_input.copy()
    co2 = text_input.copy()

    for row in text_input:
        row = row.replace('\n', '')
        for idx_row, char in enumerate(row):
            if char == '1':
                count_ones[idx_row] += 1
            else:
                count_zeroes[idx_row] += 1

    # check oxygen
    # loop through bits
    for curr_bit in range(12):
        if len(oxygen) > 1:
            count_zeroes_oxy = 0
            count_ones_oxy = 0
            for row in oxygen:
                if row[curr_bit] == '1':
                    count_ones_oxy += 1
                else:
                    count_zeroes_oxy += 1
            max_value_oxygen = '1' if count_ones_oxy >= count_zeroes_oxy else '0'
            oxygen = [elem for elem in oxygen if elem[curr_bit] == max_value_oxygen]

        if len(co2) > 1:
            count_zeroes_co2 = 0
            count_ones_co2 = 0
            for row in co2:
                if row[curr_bit] == '1':
                    count_ones_co2 += 1
                else:
                    count_zeroes_co2 += 1
            min_value_co2 = '0' if count_zeroes_co2 <= count_ones_co2 else '1'
            co2 = [elem for elem in co2 if elem[curr_bit] == min_value_co2]

    print(int(oxygen[0], 2))
    print(int(co2[0], 2))
    print(int(oxygen[0], 2) * int(co2[0], 2))
