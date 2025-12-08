from itertools import zip_longest
from common import run_input
from functools import reduce
import operator


def solution(lines):
    grid = [list(r) for r in lines]
    result = 0

    op = grid[0][-1]
    current = []

    for col in list(list(zip_longest(*grid, fillvalue=' '))) + [" "]:
        if all(c == " " for c in col):
            if op == "+":
                result += sum(current)
            else:
                result += reduce(operator.mul, current, 1)

            current = []
        else:
            current.append(int("".join(col[:-1])))
            if col[-1] != " ":
                op = col[-1]

    return result


run_input(day=6, task=2, solution=solution,
          process_line=lambda x: x.strip("\n"))
