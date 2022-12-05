import sys


def parse_input(inlines):
    stacks_line = inlines[inlines.index("\n") - 1]

    n = int(stacks_line.split("   ")[-1])

    stacks = [[] for i in range(n)]

    for ix in range(inlines.index("\n")-2, -1, -1):
        line = inlines[ix]
        for i in range(n):
            try:
                entry = line[4*i+1]
                if entry.isalpha():
                    stacks[i].append(entry)
            except IndexError:
                pass

    instructions = inlines[inlines.index("\n")+1:]

    return stacks, instructions


def execute_instructions(stacks, instructions):
    for instruction in instructions:
        instruction = instruction.strip("\n")
        number = int(instruction.split("move ")[1].split(" ")[0])
        from_n = int(instruction.split("from ")[1].split(" ")[0])
        to = int(instruction.split("to ")[1].split(" ")[0])
        for i in range(number):
            stacks[to-1].append(stacks[from_n-1].pop(-1))

    return stacks


if __name__ == "__main__":
    infile = sys.argv[1]
    stacks, instructions = parse_input(open(infile, "r").readlines())

    final_stacks = execute_instructions(stacks, instructions)

    print("".join([stack.pop(-1) for stack in final_stacks]))