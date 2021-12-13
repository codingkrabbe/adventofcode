def get_caves(connections: list):
    caves = dict()
    for connection in connections:
        if connection.cave_id_1 in caves.keys():
            caves[connection.cave_id_1]['neighbors'].append(connection.cave_id_2)
        else:
            caves[connection.cave_id_1] = {
                'neighbors': [connection.cave_id_2],
                'is_small': connection.cave_id_1.lower() == connection.cave_id_1
            }
        if connection.cave_id_2 in caves.keys():
            caves[connection.cave_id_2]['neighbors'].append(connection.cave_id_1)
        else:
            caves[connection.cave_id_2] = {
                'neighbors': [connection.cave_id_1],
                'is_small': connection.cave_id_2.lower() == connection.cave_id_2
            }
    return caves


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


walks = []


def visits_invalid(small_cave_visits: dict):
    more_than_two_visits = [small_cave_visits[cave] for cave in small_cave_visits.keys() if small_cave_visits[cave] > 2]
    two_visits = [small_cave_visits[cave] for cave in small_cave_visits.keys() if small_cave_visits[cave] == 2]
    return len(more_than_two_visits) > 0 or len(two_visits) > 1


def get_small_cave_visits(path: list):
    small_cave_visits = dict()
    for cave in path:
        if cave.lower() == cave and cave not in small_cave_visits.keys():
            small_cave_visits[cave] = 1
        elif cave.lower() == cave:
            small_cave_visits[cave] += 1
    return small_cave_visits


def get_walks(end: str, path: list, caves: dict):
    global walks
    start = path[-1]
    small_cave_visits = get_small_cave_visits(path)
    if visits_invalid(small_cave_visits):
        return None
    elif start == end:
        walks.append(path)
    elif start == 'start' and len(path) > 1:
        return None
    else:
        neighbors = caves[start]['neighbors']
        for neighbor in neighbors:
            get_walks(end, path + [neighbor], caves)
    return None


def main():
    global walks
    lines = open('input.txt', 'r').readlines()
    connections = []
    for line in lines:
        cave_id_1, cave_id_2 = line.strip().split('-')
        connections.append(Connection(cave_id_1, cave_id_2))
    caves = get_caves(connections)
    small_cave_visits = dict()
    for cave in caves.keys():
        if caves[cave]['is_small']:
            small_cave_visits[cave] = 0

    get_walks('end', ['start'], caves)
    print('Number of paths from start to end: ' + str(len(walks)))


if __name__ == '__main__':
    main()
