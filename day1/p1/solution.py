def calculate_highest_calories(input):
    max_total = 0
    total = 0
    for item in input:
        if item == "\n":
            if total > max_total:
                max_total = total
            total = 0
        else:
            total += int(item.strip("\n"))

    return max_total


if __name__ == "__main__":
    print(calculate_highest_calories(open("../input.txt", "r").readlines()))