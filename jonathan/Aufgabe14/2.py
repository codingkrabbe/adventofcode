def get_most_and_least_frequencies(first_char: str, input: dict):
    char_occurrences = {}
    for source, frequency in input.items():
        if source[-1] in char_occurrences.keys():
            char_occurrences[source[-1]] += frequency
        else:
            char_occurrences[source[-1]] = frequency
    char_occurrences[first_char] += 1
    return max(char_occurrences.values()), min(char_occurrences.values())


def get_resulting_pairs(source: str, replacement_rules: dict):
    if source in replacement_rules.keys():
        char = replacement_rules[source]
        return f'{source[0]}{char}', f'{char}{source[1]}'
    else:
        return None, None


def main():
    lines = open('input.txt', 'r').readlines()
    template = lines[0].strip()
    occurrences = {}
    last_occurrences = {}
    replacement_rules = {}
    for line in lines[2:]:
        placeholder, inserted_char = line.strip().split(' -> ')
        replacement_rules[placeholder] = inserted_char
    for j in range(len(template) - 1):
        str1, str2 = get_resulting_pairs(template[j:j + 2], replacement_rules)
        if str1 in last_occurrences.keys():
            last_occurrences[str1] += 1
        else:
            last_occurrences[str1] = 1
        if str2 in last_occurrences.keys():
            last_occurrences[str2] += 1
        else:
            last_occurrences[str2] = 1
    for i in range(39):
        print(i)
        for source in occurrences.keys():
            occurrences[source] = 0
        for source, frequency in last_occurrences.items():
            str1, str2 = get_resulting_pairs(source, replacement_rules)
            if str1 in occurrences:
                occurrences[str1] += frequency
            else:
                occurrences[str1] = frequency
            if str2 in occurrences:
                occurrences[str2] += frequency
            else:
                occurrences[str2] = frequency
        last_occurrences = occurrences.copy()
        max_occurrences, min_occurrences = get_most_and_least_frequencies(template[0], occurrences)
    expected_total_chars = len(template) * 2 ** 40 + 1 - (2 ** 40)
    actual_total_chars = sum(occurrences.values())
    print('expected:', expected_total_chars, ', actual:', actual_total_chars)
    max_occurrences, min_occurrences = get_most_and_least_frequencies(template[0], occurrences)
    print('Difference of most and least frequent character: ' + str(max_occurrences - min_occurrences))


if __name__ == '__main__':
    main()
