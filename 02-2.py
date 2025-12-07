from functools import lru_cache
from main import run_input


@lru_cache(None)
def invalid(x: int):
    s = str(x)
    n = len(s)

    for size in range(1, n):
        if n % size == 0 and s == s[:size] * (n // size):
            return True

    return False


def solution(intervals):
    total = 0
    for start, end in intervals:
        total += sum([i for i in range(int(start), int(end) + 1) if invalid(i)])
    return total


run_input(
    day=2,
    task=2,
    solution=solution,
    split=",",
    process_line=lambda x: x.split("-")
)
