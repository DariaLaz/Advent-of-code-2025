from functools import lru_cache
from main import run_input


def reduce_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    new_intervals = []

    for interval in intervals:
        if not new_intervals or new_intervals[-1][1] < interval[0]:
            new_intervals.append(interval)
        else:
            new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])

    return new_intervals


def is_in(num, intervals):
    for start, end in intervals:
        if start > num:
            return False
        if start <= num <= end:
            return True

    return False


def solution(input):
    fresh = list(
        map(lambda x: list(map(int, x.split("-"))), input[0].split("\n")))
    available = list(map(int, input[1].split("\n")))

    fresh = reduce_intervals(fresh)

    return sum(is_in(int(num), fresh) for num in available)


run_input(day=5, task=1, solution=solution, split="\n\n")
