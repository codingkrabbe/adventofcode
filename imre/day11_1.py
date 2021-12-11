def trigger_specimen_recursive(grid, x, y):
    new_flash = False
    grid[y][x]['val'] += 1
    if grid[y][x]['val'] > 9 and not grid[y][x]['flashed']:
        grid[y][x]['flashed'] = True
        for n in grid[y][x]['neighbours']:
            grid, flash = trigger_specimen_recursive(grid, n[0], n[1])
        new_flash = True
    return grid, new_flash


def iterate(grid):
    theres_flash = False
    flash_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid, flash = trigger_specimen_recursive(grid, x, y)
            theres_flash = theres_flash or flash

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]['flashed']:
                grid[y][x]['val'] = 0
                grid[y][x]['flashed'] = False
                flash_count += 1
    return grid, flash_count


lines = open('input.txt', 'r').readlines()
total_flashes, grid = 0, []
neighbour_map = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
# Read input
for l in lines:
    grid.append([{'val': int(i), 'neighbours': [], 'flashed': False} for i in list(l.strip())])
# Get neighbours
for y in range(len(grid)):
    for x in range(len(grid[0])):
        for n in neighbour_map:
            if 0 <= x + n[0] < len(grid[y]) and 0 <= y + n[1] < len(grid):
                grid[y][x]['neighbours'].append([x + n[0], y + n[1]])
for i in range(100):
    grid, flash_count = iterate(grid)
    total_flashes += flash_count
print(total_flashes)
