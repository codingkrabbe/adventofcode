NUM_DAYS = 256


def main():
    lantern_fish_timer_list = [0] * 9
    lines = open('input.txt', 'r').readlines()
    timers = lines[0].split(',')
    for timer in timers:
        timer_num = int(timer)
        lantern_fish_timer_list[timer_num] += 1
    for i in range(NUM_DAYS):
        print('Day ' + str(i + 1) + ' of ' + str(NUM_DAYS))
        num_to_spawn = lantern_fish_timer_list[0]
        tmp_list = [0] * 9
        tmp_list[8] = num_to_spawn
        for j in range(8):
            tmp_list[j] = lantern_fish_timer_list[j + 1]
        tmp_list[6] += num_to_spawn
        lantern_fish_timer_list = tmp_list
    sum = 0
    for elem in lantern_fish_timer_list:
        sum += elem
    print (sum)


if __name__ == '__main__':
    main()
