from common import run_input


def solution(grid):
    rows, cols = len(grid), len(grid[0])
    start = grid[0].index("S")

    memo = [0] * cols
    memo[start] = 1

    for r in range(rows - 1):
        new_memo = [0] * cols

        for c in range(cols):
            if memo[c] == 0:
                continue

            if grid[r + 1][c] == ".":
                new_memo[c] += memo[c]

            elif grid[r + 1][c] == "^":
                if c - 1 >= 0:
                    new_memo[c - 1] += memo[c]
                if c + 1 < cols:
                    new_memo[c + 1] += memo[c]

        memo = new_memo

    return sum(memo)


run_input(day=7, task=2, solution=solution)
