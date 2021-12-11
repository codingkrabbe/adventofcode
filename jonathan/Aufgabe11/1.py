class Octopus:
    def __init__(self, energy_level):
        self.energy_level = energy_level
        self.already_flashed = False


class OctopusGrid:
    def __init__(self, energy_levels_grid: list):
        self.height = len(energy_levels_grid)
        self.width = len(energy_levels_grid[0])
        self.grid = []
        for row in energy_levels_grid:
            grid_row = []
            for energy_level in row:
                grid_row.append(Octopus(energy_level))
            self.grid.append(grid_row)

    def increment_all_energy_levels(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].energy_level += 1

    def handle_flashes(self):
        flash_counter = 0
        for y in range(self.height):
            for x in range(self.width):
                current_octopus: Octopus = self.grid[y][x]
                if current_octopus.energy_level > 9 and not current_octopus.already_flashed:
                    flash_counter += 1
                    current_octopus.already_flashed = True
                    self.increment_surrounding_energy_levels(x, y)
        return flash_counter

    def increment_surrounding_energy_levels(self, x: int, y: int):
        for current_x in range(max(x - 1, 0), min(x + 2, self.width)):
            for current_y in range(max(y - 1, 0), min(y + 2, self.height)):
                if not (x == current_x and y == current_y):
                    self.grid[current_y][current_x].energy_level += 1

    def reset_already_flashed(self):
        for y in range(self.height):
            for x in range(self.width):
                current_octopus = self.grid[y][x]
                if current_octopus.already_flashed:
                    current_octopus.already_flashed = False
                    current_octopus.energy_level = 0


def main():
    lines = open('input.txt', 'r').readlines()
    grid = []
    for line in lines:
        number_chars = list(line.strip())
        grid.append(list(map(int, number_chars)))

    octopus_grid = OctopusGrid(grid)
    total_num_flashes = 0

    for i in range(100):
        octopus_grid.increment_all_energy_levels()
        num_flashes = octopus_grid.handle_flashes()
        total_num_flashes += num_flashes
        while num_flashes > 0:
            num_flashes = octopus_grid.handle_flashes()
            total_num_flashes += num_flashes
        octopus_grid.reset_already_flashed()

    print('Number of flashes after first 100 steps: ' + str(total_num_flashes))


if __name__ == '__main__':
    main()
