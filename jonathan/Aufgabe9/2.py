import sys


class HeightMapField:
    def __init__(self, row_idx, col_idx, value):
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.value = value

    def __eq__(self, other):
        return self.col_idx == other.col_idx and self.row_idx == other.row_idx and self.value == other.value


class HeightMap:
    def __init__(self, map: list):
        self.map = map
        self.last_row = len(map) - 1
        self.last_column = len(map[0]) - 1

    def get_basin_sizes(self):
        basin_sizes = []
        low_points = []
        for row_idx in range(self.last_row):
            for col_idx in range(self.last_column):
                if self.is_low_point(row_idx, col_idx):
                    low_points.append(HeightMapField(row_idx, col_idx, self.map[row_idx][col_idx]))
        for low_point in low_points:
            basin = [low_point]
            basin_size = 0
            while len(basin) > basin_size:
                basin_size = len(basin)
                for field in basin:
                    above_field = self.get_above_field(field.row_idx, field.col_idx)
                    left_field = self.get_left_field(field.row_idx, field.col_idx)
                    below_field = self.get_below_field(field.row_idx, field.col_idx)
                    right_field = self.get_right_field(field.row_idx, field.col_idx)
                    surrounding_fields = [above_field, left_field, below_field, right_field]
                    for surrounding_field in surrounding_fields:
                        if surrounding_field is not None and surrounding_field.value < 9 and surrounding_field not in basin:
                            basin.append(surrounding_field)
            basin_sizes.append(len(basin))
        return basin_sizes

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
        adjacent_values = []
        above_field = self.get_above_field(row, column)
        if above_field is not None:
            adjacent_values.append(above_field.value)
        left_field = self.get_left_field(row, column)
        if left_field is not None:
            adjacent_values.append(left_field.value)
        below_field = self.get_below_field(row, column)
        if below_field is not None:
            adjacent_values.append(below_field.value)
        right_field = self.get_right_field(row, column)
        if right_field is not None:
            adjacent_values.append(right_field.value)
        if value < min(adjacent_values):
            return True
        else:
            return False

    def get_above_field(self, row: int, column: int):
        if row > 0:
            return HeightMapField(row - 1, column, self.map[row - 1][column])
        else:
            return None

    def get_left_field(self, row: int, column: int):
        if column > 0:
            return HeightMapField(row, column - 1, self.map[row][column - 1])
        else:
            return None

    def get_below_field(self, row: int, column: int):
        if row < self.last_row:
            return HeightMapField(row + 1, column, self.map[row + 1][column])
        else:
            return None

    def get_right_field(self, row: int, column: int):
        if column < self.last_column:
            return HeightMapField(row, column + 1, self.map[row][column + 1])
        else:
            return None


def main():
    lines = open('input.txt', 'r').readlines()
    input_map = []
    for line in lines:
        input_map.append(list(map(int, list(line.strip()))))
    height_map = HeightMap(input_map)
    basin_sizes = height_map.get_basin_sizes()
    product = 1
    for i in range(3):
        product *= max(basin_sizes)
        basin_sizes.remove(max(basin_sizes))
    print('Product of three max basin sizes: ' + str(product))


if __name__ == '__main__':
    main()
