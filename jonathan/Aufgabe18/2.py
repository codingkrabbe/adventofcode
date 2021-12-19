import math


class RegularNumber:
    def __init__(self, value, level, index):
        self.value = value
        self.level = level
        self.index = index


class SnailNumber:
    def __init__(self, numbers: list[RegularNumber]):
        self.numbers = numbers

    def must_be_reduced(self):
        for number in self.numbers:
            if number.level >= 4 or number.value > 9:
                return True
        return False

    def reduce(self):
        while self.must_be_reduced():
            reduction_step_completed = False
            for i in range(len(self.numbers)):
                if not reduction_step_completed and self.numbers[i].level >= 4 and self.numbers[i + 1].level >= 4:  # explode
                    if i > 0:
                        self.numbers[i - 1].value += self.numbers[i].value
                    if i < len(self.numbers) - 2:
                        self.numbers[i + 2].value += self.numbers[i + 1].value
                    self.numbers[i:i + 2] = [RegularNumber(0, self.numbers[i].level - 1, i)]
                    reduction_step_completed = True
            for i in range(len(self.numbers)):
                if not reduction_step_completed and self.numbers[i].value > 9:  # split
                    left_value = math.floor(self.numbers[i].value / 2)
                    right_value = math.ceil(self.numbers[i].value / 2)
                    self.numbers[i:i + 1] = [
                        RegularNumber(left_value, self.numbers[i].level + 1, i),
                        RegularNumber(right_value, self.numbers[i].level + 1, i + 1)
                    ]
                    reduction_step_completed = True
            for i in range(len(self.numbers)):
                self.numbers[i].index = i

    def add(self, other):
        new_numbers = self.numbers + other.numbers
        for idx, number in enumerate(new_numbers):
            number.index = idx
            number.level += 1
        return SnailNumber(new_numbers)

    def get_magnitude(self):
        numbers_copy = self.numbers.copy()
        while len(numbers_copy) > 1:
            max_level_pairs: list[tuple[RegularNumber, RegularNumber]] = get_max_level_pairs(numbers_copy)
            first_pair = max_level_pairs[0]
            result = 3 * first_pair[0].value + 2 * first_pair[1].value
            new_number = RegularNumber(result, first_pair[0].level - 1, first_pair[0].index)
            numbers_copy[first_pair[0].index:first_pair[1].index + 1] = [new_number]
            for i in range(len(numbers_copy)):
                numbers_copy[i].index = i
        return numbers_copy[0].value

    def copy(self):
        return SnailNumber(self.numbers.copy())


def get_max_level_pairs(numbers: list[RegularNumber]):
    pairs = []
    max_level = max([number.level for number in numbers])
    max_level_numbers = [number for number in numbers if number.level == max_level]
    if len(max_level_numbers) % 2 != 0:
        raise ValueError('Odd number of max level numbers')
    for i in range(len(max_level_numbers) // 2):
        pairs.append((max_level_numbers[i], max_level_numbers[i + 1]))
    return pairs


def parse_snail_number(line: str):
    numbers = []
    level = -1
    for idx, char in enumerate(list(line.strip())):
        if char == '[':
            level += 1
        elif char == ']':
            level -= 1
        elif char.isnumeric():
            numbers.append(RegularNumber(int(char), level, idx))
    return SnailNumber(numbers)


def main():
    lines = open('input.txt', 'r').readlines()
    current_snail_number = parse_snail_number(lines[0])
    snail_numbers = []
    for line in lines:
        snail_numbers.append(parse_snail_number(line))
    largest_magnitude = 0
    for i in range(len(snail_numbers)):
        for j in range(len(snail_numbers)):
            if i != j:
                print(i, j)
                sum_number = snail_numbers[i].add(snail_numbers[j])
                sum_number.reduce()
                magnitude = sum_number.get_magnitude()
                if magnitude > largest_magnitude:
                    largest_magnitude = magnitude
                snail_numbers = []
                for line in lines:
                    snail_numbers.append(parse_snail_number(line))
    print('Largest magnitude:', largest_magnitude)


if __name__ == '__main__':
    main()
