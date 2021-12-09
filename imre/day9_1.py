lines = open('input.txt', 'r').readlines()
border = [10] * (len(lines[0]) + 1) # Let's sorround the dataset with 10s
grid = [border]
for l in lines:
    grid.append([10] + [int(i) for i in list(l.strip())] + [10])
grid.append(border)
summ = 0
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] < min([grid[y][x-1], grid[y][x+1], grid[y-1][x], grid[y+1][x]]):
            summ += grid[y][x] + 1
print(summ)
