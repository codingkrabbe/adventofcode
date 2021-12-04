def get_binary(most_common: bool):
    lines = open('input.txt', 'r').readlines()
    for i in range(12):
        indices_to_remove, zeros, ones = [], 0, 0
        for line in lines:
            if line[i] == '0':
                zeros += 1
            else:
                ones += 1
        for j in reversed(range(0, len(lines))):
            if zeros > ones and most_common and lines[j][i] == '1':
                lines.pop(j)
            elif zeros <= ones and most_common and lines[j][i] == '0':
                lines.pop(j)
            elif zeros > ones and not most_common and lines[j][i] == '0':
                lines.pop(j)
            elif zeros <= ones and not most_common and lines[j][i] == '1':
                lines.pop(j)
        if len(lines) == 1:
            return lines[0][:-1]


def main():
    o_binary = get_binary(True)
    co2_binary = get_binary(False)
    print(int(o_binary, 2) * int(co2_binary, 2))


if __name__ == '__main__':
    main()
