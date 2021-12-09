import sys


def read_input():
    input = {}
    with open('09-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    for y, row in enumerate(text_input):
        row = row.replace('\n', '')
        row_dict = dict()
        for x, char in enumerate(row):
            row_dict.update({x: int(char)})
        input.update({y: row_dict})

    return input


def get_risk_sum(grid: dict):
    risk_sum = 0
    len_grid = len(grid)
    len_row = len(grid[0])
    for row in grid:
        for char in grid[row]:
            is_lowest = True
            if not row - 1 < 0 and grid[row][char] >= grid[row - 1][char]:
                is_lowest = False

            if not row + 1 > len_grid - 1 and grid[row][char] >= grid[row + 1][char]:
                is_lowest = False

            if not char - 1 < 0 and grid[row][char] >= grid[row][char - 1]:
                is_lowest = False

            if not char + 1 > len_row - 1 and grid[row][char] >= grid[row][char + 1]:
                is_lowest = False

            if is_lowest:
                print('row ' + str(row) + ' grid: ' + str(char))
                risk_sum += 1 + grid[row][char]
    return risk_sum

def main():
    grid = read_input()
    risk = get_risk_sum(grid)
    print(risk)

if __name__ == '__main__':
    sys.exit(main())
