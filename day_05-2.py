from common import run_input
from day_05_common import parse_input


def is_in(num, intervals):
    for start, end in intervals:
        if start > num:
            return False
        if start <= num <= end:
            return True

    return False


def solution(input):
    fresh, _ = parse_input(input)

    return sum(end - start + 1 for start, end in fresh)


run_input(day=5, task=2, solution=solution, split="\n\n")
