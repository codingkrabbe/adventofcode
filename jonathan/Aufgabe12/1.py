def get_caves(connections: list):
    caves = set()
    for connection in connections:
        caves.add(connection.cave_id_1)
        caves.add(connection.cave_id_2)
    return caves


def is_valid_path(path: list):
    small_caves = [cave for cave in path if cave.lower() == cave]

    return len(small_caves) == len(set(small_caves))


def get_paths_between_caves_of_length_n(start: str, end: str, n: int, connections: list, curr_path: list):
    paths = []
    filtered_conns = connections.copy()
    for i in range(len(curr_path) - 1, 0, -1):
        cave = curr_path[i]
        if cave.lower() == cave:
            filtered_conns = [conn for conn in filtered_conns if conn.get_other_cave(cave) is None]

    for connection in filtered_conns:
        cave_connected_to_end = connection.get_other_cave(end)
        if cave_connected_to_end is not None:
            if n == 0 and cave_connected_to_end == start:
                return [[start] + curr_path]
            elif n > 0:
                paths += get_paths_between_caves_of_length_n(start, cave_connected_to_end, n - 1, filtered_conns,
                                                             [cave_connected_to_end] + curr_path)
    return paths


class Connection:
    def __init__(self, cave_id_1, cave_id_2):
        self.cave_id_1 = cave_id_1
        self.cave_id_2 = cave_id_2

    def get_other_cave(self, cave_id):
        if cave_id == self.cave_id_1:
            return self.cave_id_2
        elif cave_id == self.cave_id_2:
            return self.cave_id_1
        else:
            return None


def main():
    lines = open('input.txt', 'r').readlines()
    connections = []
    for line in lines:
        cave_id_1, cave_id_2 = line.strip().split('-')
        connections.append(Connection(cave_id_1, cave_id_2))
    paths = []
    for i in range(22):
        print(i)
        new_paths = get_paths_between_caves_of_length_n('start', 'end', i, connections, ['end'])
        paths += new_paths
    print('Number of paths found: ' + str(len(paths)))


if __name__ == '__main__':
    main()
