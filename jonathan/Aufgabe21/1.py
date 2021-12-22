def main():
    lines = open('input.txt', 'r').readlines()
    pos_1 = int(lines[0].strip().split()[-1])
    pos_2 = int(lines[1].strip().split()[-1])
    score_1 = 0
    score_2 = 0
    next_die_value = 1
    num_die_rolls = 0
    while score_1 < 1000 and score_2 < 1000:
        num_fields_to_move = 0
        for i in range(3):
            num_fields_to_move += next_die_value
            next_die_value += 1
            num_die_rolls += 1
            if next_die_value > 100:
                next_die_value = 1
        pos_1 = ((pos_1 + (num_fields_to_move % 10) - 1) % 10) + 1
        score_1 += pos_1
        if score_1 < 1000:
            num_fields_to_move = 0
            for i in range(3):
                num_fields_to_move += next_die_value
                next_die_value += 1
                num_die_rolls += 1
                if next_die_value > 100:
                    next_die_value = 1
            pos_2 = ((pos_2 + (num_fields_to_move % 10) - 1) % 10) + 1
            score_2 += pos_2
    losing_score = min(score_1, score_2)
    print(f'Product of losing score and die value: {losing_score * num_die_rolls}')


if __name__ == '__main__':
    main()
