import sys


def find_number_overlapping_ranges(input):
    count = 0
    for ix, line in enumerate(input):
        line = line.strip("\n")
        range1, range2 = line.split(",")
        r11, r12 = range1.split("-")
        r21, r22 = range2.split("-")
        range1 = set(range(int(r11), int(r12) + 1))
        range2 = set(range(int(r21), int(r22) + 1))

        if len(range1.intersection(range2)) > 0:
            count += 1

    return count


if __name__ == "__main__":
    infile = sys.argv[1]
    print(find_number_overlapping_ranges(open(infile, "r").readlines()))