class LanternFish:
    def __init__(self, timer = None):
        if timer is None:
            self.timer = 8
        else:
            self.timer = timer


def main():
    lantern_fish_list = []
    lines = open('input.txt', 'r').readlines()
    timers = lines[0].split(',')
    for timer in timers:
        lantern_fish_list.append(LanternFish(int(timer)))
    for i in range(80):
        to_create_counter = 0
        for lantern_fish in lantern_fish_list:
            if lantern_fish.timer == 0:
                to_create_counter += 1
                lantern_fish.timer = 6
            else:
                lantern_fish.timer -= 1
        for j in range(to_create_counter):
            lantern_fish_list.append(LanternFish())
    print(len(lantern_fish_list))


if __name__ == '__main__':
    main()
