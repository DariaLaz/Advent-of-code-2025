from functools import lru_cache
from common import run_input


def solution(input):
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    rows, cols = len(input), len(input[0])

    for r in range(rows):
        for c in range(cols):
            if input[r][c] != "@":
                continue
            count = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and input[nr][nc] == "@":
                    count += 1

            if count < 4:
                total += 1
    return total


run_input(day=4, task=1, solution=solution, process_line=list)
