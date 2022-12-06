import sys


def find_starter_marker(inlines, length=4):
    for line in inlines:
        line = line.strip("\n")
        for i in range(len(line)-length):
            if len(set(line[i:i+length])) == length:
                print(i+length)
                break

if __name__ == "__main__":
    infile = sys.argv[1]
    find_starter_marker(open(infile, "r").readlines())