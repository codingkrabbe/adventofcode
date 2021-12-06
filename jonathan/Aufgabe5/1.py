class VentField:
    def __init__(self, width: int, height: int):
        self.fields = []
        for y in range(height):
            self.fields.append([])
            for x in range(width):
                self.fields[y].append(0)

    def register_vents(self, from_x: int, from_y: int, to_x: int, to_y: int):
        if from_x == to_x or from_y == to_y:
            x_step, y_step = 1, 1
            if from_x > to_x:
                x_step = -1
                to_x -= 1
            else:
                to_x += 1
            if from_y > to_y:
                y_step = -1
                to_y -= 1
            else:
                to_y += 1
            for x in range(from_x, to_x, x_step):
                for y in range(from_y, to_y, y_step):
                    self.fields[y][x] += 1

    def get_fields_greater_than(self, threshold):
        counter = 0
        for y in range(len(self.fields)):
            for x in range(len(self.fields[0])):
                if self.fields[y][x] > threshold:
                    counter += 1
        return counter


def main():
    max_x, max_y = 0, 0
    lines = open('input.txt', 'r').readlines()
    for line in lines:
        from_to = line.split(' -> ')
        from_xy = from_to[0].split(',')
        to_xy = from_to[1].split(',')
        greater_x = max(int(from_xy[0]), int(to_xy[0]))
        greater_y = max(int(from_xy[1]), int(to_xy[1]))
        if greater_x > max_x:
            max_x = greater_x
        if greater_y > max_y:
            max_y = greater_y
    vent_field = VentField(max_x + 1, max_y + 1)
    for line in lines:
        from_to = line.split(' -> ')
        from_xy = from_to[0].split(',')
        to_xy = from_to[1].split(',')
        vent_field.register_vents(int(from_xy[0]), int(from_xy[1]), int(to_xy[0]), int(to_xy[1]))
    print(vent_field.get_fields_greater_than(1))


if __name__ == '__main__':
    main()
