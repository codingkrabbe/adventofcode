import sys


def read_content():
    with open('04-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    text_input.append('\n')
    input_grid = {}
    grid_id = 0
    new_grid = {}
    for idx, content in enumerate(text_input):
        content = content.replace('\n', '')
        if idx == 0:
            input_numbers = [int(x) for x in content.split(',')]
            continue

        if not (content):  # if empty --> separator between boards, init new grid
            if new_grid:  # grid existing from reading
                input_grid.update({grid_id: new_grid})
                grid_id += 1
            new_grid = dict()
            y_row_id = 0
            continue

        if (content):  # input numbers for grids
            x_row_list = [int(x) for x in content.strip().replace('  ', ' ').split(' ')]
            x_dict = {}
            for idx, elem in enumerate(x_row_list):
                x_dict.update({idx: elem})
            new_grid.update({y_row_id: x_dict})
            y_row_id += 1
    return input_numbers, input_grid


def get_winning_score(input_numbers: list, input_grid: list):
    num_boards = len(input_grid)
    len_x = 5
    len_y = 5

    last_result=0
    # draw numbers
    remaining_boards=input_grid
    for draw in input_numbers:
        for board_id in range(num_boards):
            for x in range(len_x):
                for y in range(len_y):
                    if input_grid[board_id][x][y] == draw:
                        input_grid[board_id][x][y] = -1
                        max_boardsum,remaining_boards = check_winner_boards(remaining_boards)
                        if max_boardsum != -1:
                            last_result= max_boardsum*draw
    return last_result


def check_winner_boards(input_grid: dict):
    '''check for bingo, return winner score of best board if successful'''
    max_board_score = -1
    remaining_boards={}
    for board_id in input_grid:
        still_valid_board=True
        board = input_grid[board_id]
        # check x winners
        for row in range(5):
            if board[0][row] == board[1][row] == board[2][row] == board[3][row] == board[4][row] == -1:
                still_valid_board=False
                board_sum = get_board_score(board)
                if board_sum > max_board_score:
                    max_board_score = board_sum
        # check y winners
        for row in range(5):
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] == board[row][4] == -1:
                still_valid_board=False
                board_sum = get_board_score(board)
                if board_sum > max_board_score:
                    max_board_score = board_sum
        if still_valid_board:
            remaining_boards.update({board_id:board})
    return max_board_score,remaining_boards


def get_board_score(board):
    board_sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                board_sum += board[i][j]
    return board_sum


def main():
    input_numbers, input_grid = read_content()
    score = get_winning_score(input_numbers, input_grid)
    print(score)


if __name__ == '__main__':
    sys.exit(main())
