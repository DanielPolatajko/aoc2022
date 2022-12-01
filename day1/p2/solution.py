import sys


def calculate_top3_highest_calories(input):
    top3 = [0, 0, 0]
    total = 0
    for item in input:
        if item == "\n":
            if total > top3[0]:
                if total > top3[1]:
                    if total > top3[2]:
                        top3[0] = top3[1]
                        top3[1] = top3[2]
                        top3[2] = total

                    else:
                        top3[0] = top3[1]
                        top3[1] = total
                else:
                    top3[0] = total
            total = 0
        else:
            total += int(item.strip("\n"))
        print(top3)

    return sum(top3)


if __name__ == "__main__":
    infile = sys.argv[1]
    print(calculate_top3_highest_calories(open(infile, "r").readlines()))