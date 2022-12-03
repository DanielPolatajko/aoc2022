import sys


def calculate_priority(x):
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96


def sum_rucksack_errors(input):
    errors = 0
    for line in input:
        line = line.strip("\n")
        halfway_point = len(line) // 2
        errors += calculate_priority(
            set(line[:halfway_point]).intersection(set(line[halfway_point:])).pop()
        )

    return errors


if __name__ == "__main__":
    infile = sys.argv[1]
    print(sum_rucksack_errors(open(infile, "r").readlines()))