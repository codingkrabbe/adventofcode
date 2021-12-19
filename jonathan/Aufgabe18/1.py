import math


class RegularNumber:
    def __init__(self, value, level):
        self.value = value
        self.level = level


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
                    self.numbers[i:i + 2] = [RegularNumber(0, self.numbers[i].level - 1)]
                    reduction_step_completed = True
            for i in range(len(self.numbers)):
                if not reduction_step_completed and self.numbers[i].value > 9:  # split
                    left_value = math.floor(self.numbers[i].value / 2)
                    right_value = math.ceil(self.numbers[i].value / 2)
                    self.numbers[i:i + 1] = [
                        RegularNumber(left_value, self.numbers[i].level + 1),
                        RegularNumber(right_value, self.numbers[i].level + 1)
                    ]
                    reduction_step_completed = True

    def add(self, other):
        new_numbers = self.numbers + other.numbers
        for number in new_numbers:
            number.level += 1
        return SnailNumber(new_numbers)

    def get_magnitude(self):
        numbers_copy = self.numbers.copy()
        max_level = max([number.level for number in numbers_copy])
        magnitude = 0
        for level in range(max_level, -1, -1):
            number_of_level_exists = max([number.level for number in numbers_copy]) == level
            while number_of_level_exists:
                reduction_step_completed = False
                for i in range(len(numbers_copy)):
                    if not reduction_step_completed and numbers_copy[i].level == level and numbers_copy[i + 1].level == level:
                        value = 3 * numbers_copy[i].value + 2 * numbers_copy[i + 1].value
                        numbers_copy[i:i + 2] = [RegularNumber(value, level - 1)]
                        reduction_step_completed = True
                number_of_level_exists = max([number.level for number in numbers_copy]) == level
        return numbers_copy[0].value


def parse_snail_number(line: str):
    numbers = []
    level = -1
    for char in list(line.strip()):
        if char == '[':
            level += 1
        elif char == ']':
            level -= 1
        elif char.isnumeric():
            numbers.append(RegularNumber(int(char), level))
    return SnailNumber(numbers)


def main():
    lines = open('input.txt', 'r').readlines()
    current_snail_number = parse_snail_number(lines[0])
    for line in lines[1:]:
        current_snail_number = current_snail_number.add(parse_snail_number(line))
        current_snail_number.reduce()
    print('Magnitude of result:', current_snail_number.get_magnitude())


if __name__ == '__main__':
    main()
