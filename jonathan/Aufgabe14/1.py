def get_most_and_least_frequencies(input: str):
    character_occurrences = dict()
    for char in list(input):
        if char in character_occurrences.keys():
            character_occurrences[char] += 1
        else:
            character_occurrences[char] = 1
    return max(character_occurrences.values()), min(character_occurrences.values())


def main():
    lines = open('input.txt', 'r').readlines()
    template = lines[0].strip()
    replacement_rules = dict()
    for line in lines[2:]:
        placeholder, inserted_char = line.strip().split(' -> ')
        replacement_rules[placeholder] = inserted_char
    for i in range(10):
        chars_to_insert = []
        for j in range(len(template) - 1):
            chars_to_insert.append(replacement_rules[template[j:j + 2]])
        for j in range(len(chars_to_insert)):
            template = template[:2 * j + 1] + chars_to_insert[j] + template[2 * j + 1:]
    max_occurrences, min_occurrences = get_most_and_least_frequencies(template)
    print('Difference of most and least frequent character: ' + str(max_occurrences - min_occurrences))



if __name__ == '__main__':
    main()
