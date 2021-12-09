def get_basin(min_point, grid):
    basin_points = {min_point}
    theres_room_to_expand = True
    while theres_room_to_expand:
        new_points = set()
        curr_size = len(basin_points)
        for p in basin_points:
            px, py = (int(p.split('|')[0]), int(p.split('|')[1]))
            for n in [[px-1, py], [px+1, py], [px, py-1], [px, py+1]]:
                if grid[n[1]][n[0]] < 9:
                    new_points.add(str(n[0]) + '|' + str(n[1]))
        basin_points = new_points | basin_points
        theres_room_to_expand = len(basin_points) > curr_size # New points have been added to the basin
    return len(basin_points)


lines = open('input.txt', 'r').readlines()
border = [10] * (len(lines[0]) + 1) # Let's sorround the dataset with 10s
grid = [border]
for l in lines:
    grid.append([10] + [int(i) for i in list(l.strip())] + [10])
grid.append(border)
min_points = []
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] < min([grid[y][x-1], grid[y][x+1], grid[y-1][x], grid[y+1][x]]):
            min_points.append(str(x) + '|' + str(y))
basins = [get_basin(p, grid) for p in min_points]
basins.sort()
product = basins[-3] * basins[-2] * basins[-1]
print(product)
