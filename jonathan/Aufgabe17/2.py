import sys


class TargetArea:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def contains(self, x: int, y: int):
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y


def hits_target_area_after_any_step(target_area: TargetArea, x_velocity: int, y_velocity: int):
    x = 0
    y = 0
    missed_by_x = x_velocity > 0 and x > target_area.max_x or x_velocity < 0 and x < target_area.min_x
    missed_by_y = y_velocity < 0 and y < target_area.min_y
    missed = missed_by_x or missed_by_y
    while not missed:
        x += x_velocity
        y += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1
        if target_area.contains(x, y):
            return True
        missed_by_x = x_velocity > 0 and x > target_area.max_x or x_velocity < 0 and x < target_area.min_x
        missed_by_y = y_velocity < 0 and y < target_area.min_y
        missed = missed_by_x or missed_by_y
    print('x =', x, ', y =', y, 'missed')
    return False


def get_x_velocity_constraints(target_area: TargetArea):
    min_x_velocity = -sys.maxsize
    max_x_velocity = sys.maxsize

    if target_area.min_x > 0:
        max_x_velocity = target_area.max_x + 1
        min_x_velocity = get_min_x_velocity(target_area.min_x) - 1
    elif target_area.max_x < 0:
        min_x_velocity = target_area.min_x - 1
        max_x_velocity = -get_min_x_velocity(-target_area.max_x) + 1
    return min_x_velocity, max_x_velocity


def get_y_velocity_constraints(target_area: TargetArea):
    min_y_velocity = target_area.min_y - 1
    max_y_velocity = get_max_y_velocity(target_area) + 1
    return min_y_velocity, max_y_velocity


def get_max_y_velocity(target_area: TargetArea):
    height = target_area.max_y - target_area.min_y
    max_y_velocity = int(height * 1.5)
    num_fails = 0
    while num_fails < 2 * height:
        current_pos_y = 0
        new_max_y_velocity = max_y_velocity + 1 + num_fails
        current_y_velocity = new_max_y_velocity
        missed = current_y_velocity < 0 and current_pos_y < target_area.min_y
        hit = False
        while not (missed or hit):
            if current_pos_y > target_area.max_y and current_y_velocity > 0:
                current_y_velocity = -current_y_velocity
            current_pos_y += current_y_velocity
            current_y_velocity -= 1
            missed = current_y_velocity < 0 and current_pos_y < target_area.min_y
            hit = current_y_velocity < 0 and target_area.min_y <= current_pos_y <= target_area.max_y
        if missed:
            num_fails += 1
        if hit:
            num_fails = 0
            max_y_velocity = new_max_y_velocity
    return max_y_velocity


def get_min_x_velocity(min_x: int):
    counter = 0
    pos_sum = 0
    while pos_sum < min_x:
        print(pos_sum, '<', min_x, ', trying one higher')
        counter += 1
        pos_sum += counter
    return counter


def main():
    lines = open('input.txt', 'r').readlines()
    split = lines[0].split()
    x_str = split[-2]
    y_str = split[-1]
    min_x, max_x = map(int, x_str[2:-1].split('..'))
    min_y, max_y = map(int, y_str[2:].split('..'))
    target_area = TargetArea(min_x, min_y, max_x, max_y)
    min_x_velocity, max_x_velocity = get_x_velocity_constraints(target_area)
    num_distinct_velocities = 0
    for x_velocity in range(min_x_velocity, max_x_velocity):
        min_y_velocity, max_y_velocity = get_y_velocity_constraints(target_area)
        for y_velocity in range(min_y_velocity, max_y_velocity):
            if hits_target_area_after_any_step(target_area, x_velocity, y_velocity):
                num_distinct_velocities += 1
    print('Number of distinct velocities:', num_distinct_velocities)



if __name__ == '__main__':
    main()
