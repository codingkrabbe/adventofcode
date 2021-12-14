import numpy as np
lines = open('input.txt', 'r').readlines()
max_x = max([int(line.strip().split(',')[0]) for line in lines if ',' in line])
max_y = max([int(line.strip().split(',')[1]) for line in lines if ',' in line])
grid = np.zeros((max_y + 1, max_x + 1), dtype='int32')
ops = []
# parse data
for line in lines:
    if ',' in line:
        x, y = tuple([int(c) for c in line.strip().split(',')])
        grid[y, x] = 1
    if '=' in line:
        ops.append({'axis': line[11], 'val': int(line.strip().split('=')[1])})


def fold(axis: str, value: int, matrix):
    if axis == 'x':
        matrix = np.rot90(matrix) # Rotate matrix
    above_fold = matrix[:value, :]
    below_fold = matrix[value + 1:, :]
    above_fold[above_fold.shape[0] - below_fold.shape[0]:, :] += np.flip(below_fold, axis=0)
    matrix = above_fold
    if axis == 'x':
        matrix = np.rot90(matrix, 3) # Rotate back
    return matrix


print(np.count_nonzero(fold(ops[0]['axis'], ops[0]['val'], grid)))
