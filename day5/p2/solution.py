import sys

from p1.solution import parse_input

def execute_instructions(stacks, instructions):
    for instruction in instructions:

        instruction = instruction.strip("\n")

        number = int(instruction.split("move ")[1].split(" ")[0])
        from_n = int(instruction.split("from ")[1].split(" ")[0])
        to = int(instruction.split("to ")[1].split(" ")[0])

        stacks[to-1] += stacks[from_n-1][-1*number:]
        stacks[from_n-1] = stacks[from_n-1][:-1*number]

    return stacks


if __name__ == "__main__":
    infile = sys.argv[1]
    stacks, instructions = parse_input(open(infile, "r").readlines())

    final_stacks = execute_instructions(stacks, instructions)

    print("".join([stack.pop(-1) for stack in final_stacks]))