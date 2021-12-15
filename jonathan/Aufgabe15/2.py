import networkx as nx


def get_edges(matrix: list, x_pos: int, y_pos: int):
    edges = []

    for y in range(max(y_pos - 1, 0), min(y_pos + 2, len(matrix))):
        for x in range(max(x_pos - 1, 0), min(x_pos + 2, len(matrix[0]))):
            if (not (x == x_pos and y == y_pos)) and (x == x_pos or y == y_pos):
                edges.append((f'{x_pos}-{y_pos}', f'{x}-{y}', matrix[y][x]))
    return edges


def main():
    lines = open('input.txt', 'r').readlines()
    starting_matrix = []
    for line in lines:
        row = []
        for x in line.strip():
            row.append(int(x))
        starting_matrix.append(row)
    full_matrix = []
    for y in range(len(starting_matrix) * 5):
        row = []
        for x in range(len(starting_matrix) * 5):
            row.append(-1)
        full_matrix.append(row)
    for y_tile_idx in range(5):
        for x_tile_idx in range(5):
            for y in range(len(starting_matrix)):
                for x in range(len(starting_matrix[0])):
                    y_idx = y + y_tile_idx * len(starting_matrix)
                    x_idx = x + x_tile_idx * len(starting_matrix[0])
                    full_matrix[y_idx][x_idx] = starting_matrix[y][x] + y_tile_idx + x_tile_idx
                    curr_val = full_matrix[y_idx][x_idx]
                    if curr_val > 9:
                        full_matrix[y_idx][x_idx] = curr_val - 9 * (curr_val // 9)

    edge_list = []
    for y in range(len(full_matrix)):
        for x in range(len(full_matrix[0])):
            new_edges = get_edges(full_matrix, x, y)
            edge_list += new_edges
    g = nx.DiGraph()
    for edge in edge_list:
        g.add_edge(edge[0], edge[1], weight=edge[2])
    source_node_name = '0-0'
    target_node_name = f'{str(len(full_matrix[0]) - 1)}-{str(len(full_matrix) - 1)}'
    shortest_path = nx.shortest_path(g, source_node_name, target_node_name, 'weight')
    shortest_path_length = nx.shortest_path_length(g, source_node_name, target_node_name, 'weight')
    print('Shortest path length:', str(shortest_path_length))


if __name__ == '__main__':
    main()
