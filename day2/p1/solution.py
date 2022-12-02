import sys


def calculate_score(input):
    score = 0
    for line in input:
        opponent, play = line.strip("\n").split(" ")
        if play == "X":
            score += 1
            if opponent == "A":
                score += 3
            if opponent == "C":
                score += 6
        elif play == "Y":
            score += 2
            if opponent == "B":
                score += 3
            if opponent == "A":
                score += 6
        elif play == "Z":
            score += 3
            if opponent == "B":
                score += 6
            if opponent == "C":
                score += 3
    return score


if __name__ == "__main__":
    infile = sys.argv[1]
    print(calculate_score(open(infile, "r").readlines()))