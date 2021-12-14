from PIL import Image, ImageDraw, ImageFont

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


def print_animation(grid, i):
    color_dict = {0: '██', 1: '░░', 2: '░░', 3: '░░', 4: '░░', 5: '▒▒', 6: '▒▒', 7: '▒▒', 8: '▒▒', 9: '▒▒'}
    text = ''
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            text += color_dict[grid[y][x]['val']]
        text += '\n'
    image = Image.new(mode="RGB", size=(360, 360), color='black')
    fnt = ImageFont.truetype('consolai.ttf', 15)
    draw = ImageDraw.Draw(image)
    draw.text((10, 30), text, font=fnt)
    image.save('images/img' + str(i) + '.png')


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
for i in range(500):
    grid, flash_count = iterate(grid)
    print_animation(grid, i)
    if flash_count == 100:
        print(i + 1)
