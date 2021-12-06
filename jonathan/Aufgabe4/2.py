BINGO_BOARD_LENGTH = 5


class BingoField:
    def __init__(self, number):
        self.number = number
        self.marked = False


class BingoBoard:
    def __init__(self, numbers: list):
        self.board = [[], [], [], [], []]
        self.already_won = False

        for row_idx, _ in enumerate(numbers):
            for number in numbers[row_idx]:
                self.board[row_idx].append(BingoField(int(number)))

    def mark_number(self, number):
        for row in self.board:
            for bingo_field in row:
                if bingo_field.number == number:
                    bingo_field.marked = True
                    self.check_for_win()

    def check_for_win(self):
        for row in self.board:
            all_marked = True
            for bingo_field in row:
                if not bingo_field.marked:
                    all_marked = False
            if all_marked:
                self.already_won = True
        for col_idx in range(len(self.board[0])):
            all_marked = True
            for row_idx in range(len(self.board)):
                if not self.board[row_idx][col_idx].marked:
                    all_marked = False
            if all_marked:
                self.already_won = True

    def calculate_score(self, last_marked_number):
        score = 0
        for row in self.board:
            for bingo_field in row:
                if not bingo_field.marked:
                    score += bingo_field.number
        return score * last_marked_number


def read_bingo_boards(lines: list):
    bingo_boards = []
    current_board_numbers = []

    for line in lines:
        if not line.strip() == '':
            current_board_numbers.append(line.strip().split())
            if len(current_board_numbers) == BINGO_BOARD_LENGTH:
                bingo_boards.append(BingoBoard(current_board_numbers))
                current_board_numbers = []
    return bingo_boards


def main():
    lines = open('input.txt', 'r').readlines()
    drawn_numbers = lines[0].split(',')
    bingo_boards = read_bingo_boards(lines[2:])
    board_to_check = None
    score_printed = False
    for drawn_number in drawn_numbers:
        if not score_printed:
            for bingo_board in bingo_boards:
                bingo_board.mark_number(int(drawn_number))
            boards_not_yet_won = []
            for bingo_board in bingo_boards:
                if board_to_check is None and not bingo_board.already_won:
                    boards_not_yet_won.append(bingo_board)
            if board_to_check is None and len(boards_not_yet_won) == 1:
                board_to_check = boards_not_yet_won[0]
            if board_to_check is not None:
                if board_to_check.already_won:
                    print(board_to_check.calculate_score(int(drawn_number)))
                    score_printed = True


if __name__ == '__main__':
    main()
