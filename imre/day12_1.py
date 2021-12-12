lines = open('input.txt', 'r').readlines()
nodes = {}
complete_walks = []
# parse graph
for l in lines:
    edge = l.strip().split('-')
    for i in [0, 1]:
        node, other = (edge[i], edge[{1: 0, 0: 1}[i]])
        if node not in nodes:
            nodes[node] = {'name': node, 'big': node == node.upper(), 'neighbours': [other]}
        else:
            nodes[node]['neighbours'].append(other)


def recursive_walk(node, nodes, walk):
    if node in walk and not nodes[node]['big']:
        return False
    w = walk.copy()
    w.append(node)
    if node == 'end':
        global complete_walks
        complete_walks.append(w)
        return False
    for n in nodes[node]['neighbours']:
        recursive_walk(n, nodes, w)


recursive_walk('start', nodes, [])
print(len(complete_walks))
