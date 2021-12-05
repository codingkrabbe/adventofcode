import sys

len_x = 1000
len_y = 1000
file = '05-input.txt'


def create_grid():
    grid = {}
    for x in range(len_x):
        row = dict()
        for y in range(len_y):
            row.update({y: 0})
        grid.update({x: row})
    return grid


def read_input(grid: dict):
    output_grid = grid.copy()
    coordinates = []
    with open('05-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()

    for row in text_input:
        single_coordinate = [int(x) for x in row.strip().replace(' -> ', ',').split(',')]
        coordinates.append(single_coordinate)

    for line in coordinates:
        if line[0] != line[2] and line[1] != line[3]:
            continue  # ignore sloped for now

        # identify traversal direction
        if line[0] == line[2]:  # x stays the same
            start_value = min([line[1], line[3]])
            end_value = max([line[1], line[3]])

            for i in range(start_value, end_value + 1):  # includes endpoints
                curr_value = output_grid[line[0]][i]
                output_grid[line[0]][i] = curr_value + 1

        if line[1] == line[3]:  # y stays the same
            start_value = min([line[0], line[2]])
            end_value = max([line[0], line[2]])

            for i in range(start_value, end_value + 1):  # includes endpoints
                curr_value = output_grid[i][line[1]]
                output_grid[i][line[1]] = curr_value + 1

    return output_grid


def get_danger_zones(grid: dict):
    num_danger_zones = 0
    for x in range(len_x):
        for y in range(len_y):
            if grid[x][y] > 1:
                num_danger_zones += 1
    return num_danger_zones


def main():
    grid = create_grid()
    grid_with_input = read_input(grid)
    num_of_danger_zones = get_danger_zones(grid_with_input)
    print(num_of_danger_zones)


if __name__ == '__main__':
    sys.exit(main())
