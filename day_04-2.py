from functools import lru_cache
from common import run_input


def solution(input):
    total = 0
    last_count = -1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    rows, cols = len(input), len(input[0])
    rolls = set((r, c) for r in range(rows)
                for c in range(cols) if input[r][c] == "@")

    while last_count != len(rolls):
        last_count = len(rolls)
        for r, c in rolls.copy():
            count = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in rolls:
                    count += 1

            if count < 4:
                rolls.remove((r, c))
                total += 1

    return total


run_input(day=4, task=2, solution=solution, process_line=list)
