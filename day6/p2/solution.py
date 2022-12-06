import sys
from p1.solution import find_starter_marker

if __name__ == "__main__":
    infile = sys.argv[1]
    find_starter_marker(open(infile, "r").readlines(), length=14)