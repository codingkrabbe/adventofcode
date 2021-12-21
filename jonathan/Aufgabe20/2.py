NUM_STEPS = 50


def append_n_unlit_rows(grid: list[list[str]], n: int, length: int):
    for i in range(n):
        row = []
        for j in range(length):
            row.append('.')
        grid.append(row)


def append_n_lit_rows(grid: list[list[str]], n: int, length: int, append_type: str):
    if append_type != 'full':
        for i in range(n):
            row = []
            for j in range(length):
                row.append('#')
            grid.append(row)
    elif append_type == 'full':
        for i in range(1):
            row = []
            for j in range(length):
                row.append('#')
            grid.append(row)
        for i in range(1, n - 1):
            row = ['#']
            for j in range(length - 2):
                row.append('.')
            row += ['#']
            grid.append(row)
        for i in range(1):
            row = []
            for j in range(length):
                row.append('#')
            grid.append(row)




def main():
    lines = open('input.txt', 'r').readlines()
    algorithm = lines[0]
    grid = []
    for line in lines[2:]:
        grid.append(list(line.strip()))
    for step in range(NUM_STEPS):
        should_add_lit = algorithm[0] == '#' and step % 2 == 1
        reference_grid = []
        if should_add_lit:
            append_n_lit_rows(reference_grid, 2, len(grid[0]) + 4, 'start')
        else:
            append_n_unlit_rows(reference_grid, 2, len(grid[0]) + 4)
        for row in grid:
            if should_add_lit:
                new_row = ['#', '#']
            else:
                new_row = ['.', '.']
            for element in row:
                new_row.append(element)
            if should_add_lit:
                new_row += ['#', '#']
            else:
                new_row += ['.', '.']
            reference_grid.append(new_row)
        if should_add_lit:
            append_n_lit_rows(reference_grid, 2, len(grid[0]) + 4, 'end')
        else:
            append_n_unlit_rows(reference_grid, 2, len(grid[0]) + 4)
        new_grid = []
        append_n_unlit_rows(new_grid, len(reference_grid) - 2, len(reference_grid[0]) - 2)
        for y in range(1, len(reference_grid) - 1):
            for x in range(1, len(reference_grid[0]) - 1):
                binary_digits_list = reference_grid[y - 1][x - 1:x + 2] \
                                + reference_grid[y][x - 1:x + 2] \
                                + reference_grid[y + 1][x - 1:x + 2]
                binary_digits_string = ''.join(binary_digits_list).replace('.', '0').replace('#', '1')
                index = int(binary_digits_string, 2)
                new_grid[y - 1][x - 1] = algorithm[index]
        blub = 0
        grid = new_grid
    lit_pixels = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                lit_pixels += 1
    print(f'Number of lit pixels: {lit_pixels}')


if __name__ == '__main__':
    main()
