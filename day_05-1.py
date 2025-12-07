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
    fresh, available = parse_input(input)

    return sum(is_in(int(num), fresh) for num in available)


run_input(day=5, task=1, solution=solution, split="\n\n")
