import numpy as np
import pickle
from os.path import exists
#Init
lines = open('input.txt', 'r').readlines()
big_num = np.iinfo(np.uint32).max
pickle_file_name = 'day15.dat'
border = [big_num] * (len(lines[0]) + 1) # Let's sorrund the dataset with big numbers so we don't need to check edges
grid = [border]
for l in lines:
    grid.append([big_num] + [int(i) for i in list(l.strip())] + [big_num])
grid.append(border)
grid = np.array(grid, dtype='uint32')
start, end = (1, 1), (grid.shape[0] - 2, grid.shape[1] - 2) # Coordinates for the start and end positions
directions = {'↓': np.array([1, 0]), '→': np.array([0, 1]), '↑': np.array([-1, 0]), '←': np.array([0, -1])}
reverse = {'←': '→', '→': '←', '↑': '↓', '↓': '↑', 'o': ''}
best_walk = {}
# Init tally grid to record lowest risk tally on any path when stepping there.
# Also min risk full path (best solution so far)
if exists(pickle_file_name) and False:
    with open(pickle_file_name, 'rb') as f:
        tally_grid, min_risk_level = pickle.load(f)
else:
    tally_grid = np.ones(grid.shape, dtype='uint32') * big_num
    # Build naive straight path
    min_risk_level = 0
    pos = start
    i = 0
    while pos != end:
        if i % 2 == 0:
            pos = (pos[0] + 1, pos[1])
        else:
            pos = (pos[0], pos[1] + 1)
        min_risk_level += grid[pos]
        i += 1


def recursive_walk(position, risk_map, walk):
    # Check if we were here already
    if position in walk['positions'][:-1]:
        return False
    # Check if there is already a better path found to this position.
    global tally_grid
    if walk['tally'] > tally_grid[position]:
        return False
    else:
        tally_grid[position] = walk['tally']
    # Check if there is a better solution than the current tally.
    global min_risk_level
    if walk['tally'] > min_risk_level:
        # This is a bad path. time to give up
        return False
    # Check if we arrived
    if position == end:
        if walk['tally'] < min_risk_level:
            min_risk_level = walk['tally']
            global best_walk
            best_walk = walk.copy()
            print('Found a better solution! Tally:', walk['tally'],
                  'Grid mapped:', int(np.count_nonzero(tally_grid < big_num) / (end[0] * end[1]) * 100), '%')
            with open(pickle_file_name, 'wb') as f:
                pickle.dump((tally_grid, min_risk_level), f, pickle.HIGHEST_PROTOCOL)
        return False
    # Ok, let's go further
    for d in directions.keys():
        # It's never a good idea to go back
        if d == reverse[walk['steps'][-1]]:
            continue
        next_pos = tuple(np.array(position) + directions[d])
        w = walk.copy()
        w['tally'] += risk_map[next_pos]
        w['steps'] = w['steps'] + [d]
        w['positions'] = w['positions'] + [next_pos]
        recursive_walk(next_pos, risk_map, w)


recursive_walk(start, grid, {'tally': 0, 'steps': ['o'], 'positions': []})
print(best_walk)
