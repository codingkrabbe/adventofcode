import functools

FREQUENCIES = (1, 3, 6, 7, 6, 3, 1)
VALUES = (3, 4, 5, 6, 7, 8, 9)


@functools.lru_cache(maxsize=None)
def perform_turn(pos_1, score_1, pos_2, score_2):
    if score_1 >= 21:
        return 1, 0
    if score_2 >= 21:
        return 0, 1

    total_wins_1 = 0
    total_wins_2 = 0

    for i in range(len(FREQUENCIES)):
        new_pos_1 = (pos_1 + VALUES[i] - 1) % 10 + 1
        new_score_1 = score_1 + new_pos_1
        wins_2, wins_1 = perform_turn(pos_2, score_2, new_pos_1, new_score_1)
        total_wins_1 += wins_1 * FREQUENCIES[i]
        total_wins_2 += wins_2 * FREQUENCIES[i]

    return total_wins_1, total_wins_2



def main():
    lines = open('input.txt', 'r').readlines()
    pos_1 = int(lines[0].strip().split()[-1])
    pos_2 = int(lines[1].strip().split()[-1])
    score_1 = 0
    score_2 = 0
    universes_won_1, universes_won_2 = perform_turn(pos_1, score_1, pos_2, score_2)
    max_universes_won = max(universes_won_1, universes_won_2)
    print(f'Max universes won: {max_universes_won}')


if __name__ == '__main__':
    main()
