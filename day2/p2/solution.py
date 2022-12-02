import sys


def calculate_score(input):
    score = 0
    for line in input:
        opponent, play = line.strip("\n").split(" ")
        if play == "X":
            if opponent == "A":
                score += 3
            if opponent == "B":
                score += 1
            if opponent == "C":
                score += 2
        elif play == "Y":
            score += 3
            if opponent == "A":
                score += 1
            if opponent == "B":
                score += 2
            if opponent == "C":
                score += 3
        elif play == "Z":
            score += 6
            if opponent == "A":
                score += 2
            if opponent == "B":
                score += 3
            if opponent == "C":
                score += 1
    return score


if __name__ == "__main__":
    infile = sys.argv[1]
    print(calculate_score(open(infile, "r").readlines()))