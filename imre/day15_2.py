import networkx as nx
import numpy as np

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
lines = open('input.txt', 'r').readlines()
G = nx.DiGraph()
grid = []
for l in lines:
    grid.append([int(i) for i in list(l.strip())])

# Compile large grid
grid = np.array(grid)
big_grid = grid.copy()
for i in range(1, 5):
    for x in np.nditer(grid, op_flags=['readwrite']):
        x[...] = (x[...] + 1) % 9
        if x[...] == 0: x[...] = 9
    big_grid = np.hstack((big_grid, grid))
grid = big_grid.copy()
for i in range(1, 5):
    for x in np.nditer(grid, op_flags=['readwrite']):
        x[...] = (x[...] + 1) % 9
        if x[...] == 0: x[...] = 9
    big_grid = np.vstack((big_grid, grid))
grid = big_grid.copy()

#Construct graph
a = grid.shape[0]
for y in range(a):
    for x in range(a):
        node_id = str(x) + '|' + str(y)
        G.add_node(node_id)
edges = []
for y in range(a):
    for x in range(a):
        node_id = str(x) + '|' + str(y)
        for d in directions:
            neighbour_y = y + d[0]
            neighbour_x = x + d[1]
            neighbour_id = str(neighbour_x) + '|' + str(neighbour_y)
            if 0 <= neighbour_x <= a - 1 and 0 <= neighbour_y <= a - 1:
               edges.append((node_id, neighbour_id, {'weight': grid[neighbour_y][neighbour_x]}))
G.add_edges_from(edges)

# Icing on the cake
path = nx.shortest_path(G, source='0|0', target=str(a - 1) + '|' + str(a - 1), weight='weight')
print(path)
score = sum([grid[int(p.split('|')[1])][int(p.split('|')[0])] for p in path[1:]])
print(score)
