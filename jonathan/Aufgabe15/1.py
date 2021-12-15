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
    matrix = []
    for line in lines:
        row = []
        for x in line.strip():
            row.append(int(x))
        matrix.append(row)
    edge_list = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            new_edges = get_edges(matrix, x, y)
            edge_list += new_edges
    g = nx.DiGraph()
    for edge in edge_list:
        g.add_edge(edge[0], edge[1], weight=edge[2])
    source_node_name = '0-0'
    target_node_name = f'{str(len(matrix[0]) - 1)}-{str(len(matrix) - 1)}'
    shortest_path = nx.shortest_path(g, source_node_name, target_node_name, 'weight')
    shortest_path_length = nx.shortest_path_length(g, source_node_name, target_node_name, 'weight')
    print('Shortest path length:', str(shortest_path_length))


if __name__ == '__main__':
    main()
