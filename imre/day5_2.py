lines = open('input.txt', 'r').readlines()
point_list = {}

def line_to_points(x_1, y_1, x_2, y_2):
    points = []
    if x_1 == x_2:
        for i in range(min(y_1, y_2), max(y_1, y_2) + 1):
            points.append([x_1, i])
    elif y_1 == y_2:
        for i in range(min(x_1, x_2), max(x_1, x_2) + 1):
            points.append([i, y_1])
    elif abs(x_1 - x_2) == abs(y_1 - y_2):
        if x_1 < x_2 and y_1 < y_2:
            for i in range(abs(x_1 - x_2) + 1):
                points.append([x_1 + i, y_1 + i])
        if x_1 < x_2 and y_1 > y_2:
            for i in range(abs(x_1 - x_2) + 1):
                points.append([x_1 + i, y_1 - i])
        if x_1 > x_2 and y_1 < y_2:
            for i in range(abs(x_1 - x_2) + 1):
                points.append([x_1 - i, y_1 + i])
        if x_1 > x_2 and y_1 > y_2:
            for i in range(abs(x_1 - x_2) + 1):
                points.append([x_1 - i, y_1 - i])
    else:
        return []
    return points


for l in lines:
    x1, y1, x2, y2 = tuple([int(n) for n in l.replace(' -> ', ',').split(',')])
    for p in line_to_points(x1, y1, x2, y2):
        point_id = str(p[0]) + ',' + str(p[1])
        if point_id in point_list:
            point_list[str(p[0]) + ',' + str(p[1])] += 1
        else:
            point_list[point_id] = 1
counter = len([point_list[p] for p in point_list.keys() if point_list[p] >= 2])
print(counter)




