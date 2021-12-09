import sys


class HeightMap:
    def __init__(self, map: list):
        self.map = map
        self.last_row = len(map) - 1
        self.last_column = len(map[0]) - 1

    def calculate_danger_level_sum(self):
        sum = 0
        for row_idx in range(self.last_row + 1):
            for col_idx in range(self.last_column + 1):
                if self.is_low_point(row_idx, col_idx):
                    sum += self.get_danger_level(row_idx, col_idx)
        return sum

    def get_danger_level(self, row: int, column: int):
        return self.map[row][column] + 1

    def is_low_point(self, row: int, column: int):
        value = self.map[row][column]
        above_value = self.get_above_value(row, column)
        left_value = self.get_left_value(row, column)
        below_value = self.get_below_value(row, column)
        right_value = self.get_right_value(row, column)
        adjacent_values = [above_value, left_value, below_value, right_value]
        if value < min(adjacent_values):
            return True
        else:
            return False

    def get_above_value(self, row: int, column: int):
        if row > 0:
            return self.map[row - 1][column]
        else:
            return sys.maxsize

    def get_left_value(self, row: int, column: int):
        if column > 0:
            return self.map[row][column - 1]
        else:
            return sys.maxsize

    def get_below_value(self, row: int, column: int):
        if row < self.last_row:
            return self.map[row + 1][column]
        else:
            return sys.maxsize

    def get_right_value(self, row: int, column: int):
        if column < self.last_column:
            return self.map[row][column + 1]
        else:
            return sys.maxsize


def main():
    lines = open('input.txt', 'r').readlines()
    input_map = []
    for line in lines:
        input_map.append(list(map(int, list(line.strip()))))
    height_map = HeightMap(input_map)
    danger_level_sum = height_map.calculate_danger_level_sum()
    print('Sum of low point danger levels: ' + str(danger_level_sum))


if __name__ == '__main__':
    main()
