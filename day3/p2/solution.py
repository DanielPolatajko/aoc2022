import sys

from p1.solution import calculate_priority


def calculate_badge_sum(input):
    badge_sum = 0
    for i in range(len(input) // 6):
        lines = [line.strip("\n") for line in input[i * 6:(i + 1) * 6]]
        badge1 = set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2])).pop()
        badge2 = set(lines[3]).intersection(set(lines[4])).intersection(set(lines[5])).pop()

        badge_sum += calculate_priority(badge1) + calculate_priority(badge2)

    return badge_sum


if __name__ == "__main__":
    infile = sys.argv[1]
    print(calculate_badge_sum(open(infile, "r").readlines()))