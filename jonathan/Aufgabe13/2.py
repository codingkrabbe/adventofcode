class Paper:
    def __init__(self, sheet: list):
        self.sheet = sheet
        self.width = len(sheet[0])
        self.height = len(sheet)

    def fold_x(self, fold_position: int):
        new_sheet = []
        for y in range(self.height):
            row = []
            for x in range(fold_position):
                row.append(self.sheet[y][x])
            new_sheet.append(row)
        for y in range(self.height):
            for x in range(1, fold_position + 1):
                new_sheet[y][fold_position - x].marked = new_sheet[y][fold_position - x].marked \
                                                         or self.sheet[y][fold_position + x].marked
        self.sheet = new_sheet
        self.width = len(new_sheet[0])

    def fold_y(self, fold_position: int):
        new_sheet = []
        for y in range(fold_position):
            row = []
            for x in range(self.width):
                row.append(self.sheet[y][x])
            new_sheet.append(row)
        for y in range(1, fold_position + 1):
            for x in range(self.width):
                new_sheet[fold_position - y][x].marked = new_sheet[fold_position - y][x].marked \
                                                         or self.sheet[fold_position + y][x].marked
        self.sheet = new_sheet
        self.height = len(new_sheet)

    def get_num_points(self):
        num_points = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.sheet[y][x].marked:
                    num_points += 1
        return num_points


class SheetField:
    def __init__(self, marked: bool):
        self.marked = marked


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class FoldInstruction:
    def __init__(self, axis: str, position: int):
        self.axis = axis
        self.position = position


def get_max_coordinates(coordinates: list):
    max_x = 0
    max_y = 0
    for coordinate in coordinates:
        max_x = max(max_x, coordinate.x)
        max_y = max(max_y, coordinate.y)
    return max_x, max_y


def main():
    lines = open('input.txt', 'r').readlines()
    coordinates = []
    fold_instructions = []
    coordinates_parsed = False
    for line in lines:
        stripped_line = line.strip()
        if stripped_line != '' and not coordinates_parsed:
            x, y = stripped_line.split(',')
            coordinates.append(Coordinate(int(x), int(y)))
        elif stripped_line != '' and coordinates_parsed:
            axis, position = stripped_line.split(' ')[2].split('=')
            fold_instructions.append(FoldInstruction(axis, int(position)))
        else:
            coordinates_parsed = True
    max_x, max_y = get_max_coordinates(coordinates)
    input_matrix = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(SheetField(False))
        input_matrix.append(row)
    for coordinate in coordinates:
        input_matrix[coordinate.y][coordinate.x].marked = True
    paper_sheet = Paper(input_matrix)
    for fold_instruction in fold_instructions:
        if fold_instruction.axis == 'x':
            paper_sheet.fold_x(fold_instruction.position)
        elif fold_instruction.axis == 'y':
            paper_sheet.fold_y(fold_instruction.position)
    for y in range(paper_sheet.height):
        output = ''
        for x in range(paper_sheet.width):
            if paper_sheet.sheet[y][x].marked:
                output += '# '
            else:
                output += '. '
        print(output)


if __name__ == '__main__':
    main()
