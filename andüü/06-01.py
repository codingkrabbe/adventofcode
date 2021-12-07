import sys

age_buckets = 9


def read_input():
    with open('06-input.txt', 'r', encoding='utf-8') as f:
        text_input = f.readlines()
    list_input = text_input[0].split(',')
    return list_input


def fill_buckets(input: list):
    buckets = {}
    for i in range(age_buckets):
        buckets.update({i: 0})

    for fish in input:
        old_value = buckets[int(fish)]
        buckets[int(fish)] = old_value + 1
    return buckets

def multiply_fishies(buckets: dict, cycles:int):

    cbuckets = buckets # copy by value
    for cycle in range(cycles):
        new_buckets = dict()
        for i in range(age_buckets):

            if i < 6:
                new_buckets.update({i: cbuckets[i+1]})
            if i == 6:
                new_buckets.update({i: cbuckets[i+1] + cbuckets[0]})
            if i == 7:
                new_buckets.update({i: cbuckets[i + 1]})
            if i == 8:
                new_buckets.update({i: cbuckets[0]})
        cbuckets = new_buckets

    return new_buckets


def main():
    input = read_input()
    buckets = fill_buckets(input)
    new_buckets = multiply_fishies(buckets, 256)
    print(sum(new_buckets.values()))


if __name__ == '__main__':
    sys.exit(main())
