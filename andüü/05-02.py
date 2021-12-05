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
        # sloped left top to right bottom
        if (line[0] < line[2] and line[1] < line[3]) or (line[0] > line[2] and line[1] > line[3]):
            start_x = min([line[0], line[2]])
            start_y = min([line[1], line[3]])
            delta = abs(line[0] - line[2]) + 1

            for i in range(delta):
                curr_value = output_grid[start_x + i][start_y + i]
                output_grid[start_x + i][start_y + i] = curr_value + 1

        # sloped left bottom to top right
        elif (line[0] < line[2] and line[1] > line[3]) or (line[0] > line[2] and line[1] < line[3]):
            start_x = min([line[0], line[2]])
            start_y = max([line[1], line[3]])
            delta = abs(line[0] - line[2]) + 1
            for i in range(delta):
                curr_value = output_grid[start_x + i][start_y - i]
                output_grid[start_x + i][start_y - i] = curr_value + 1
        # x stays the same
        elif line[0] == line[2]:
            start_value = min([line[1], line[3]])
            end_value = max([line[1], line[3]])

            for i in range(start_value, end_value + 1):  # includes endpoints
                curr_value = output_grid[line[0]][i]
                output_grid[line[0]][i] = curr_value + 1

        # y stays the same
        elif line[1] == line[3]:
            start_value = min([line[0], line[2]])
            end_value = max([line[0], line[2]])

            for i in range(start_value, end_value + 1):  # includes endpoints
                curr_value = output_grid[i][line[1]]
                output_grid[i][line[1]] = curr_value + 1
        else:
            print(line)
    return output_grid


def get_danger_zones(grid: dict):
    num_danger_zones = 0
    for x in range(len_x):
        for y in range(len_y):
            if grid[x][y] > 1:
                num_danger_zones += 1
    return num_danger_zones

def print_grid(grid:dict):
    grid_list=[]
    for x in range(len_x):
        row=[]
        for y in range(len_y):
            row.append(str(grid[y][x]).replace('0','.'))
        grid_list.append(row)
        print(row)

def main():
    grid = create_grid()
    grid_with_input = read_input(grid)
    # print_grid(grid_with_input)
    num_of_danger_zones = get_danger_zones(grid_with_input)
    print(num_of_danger_zones)


if __name__ == '__main__':
    sys.exit(main())
