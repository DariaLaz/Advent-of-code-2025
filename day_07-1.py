from common import run_input


def solution(grid):
    rows, cols = len(grid), len(grid[0])

    stack = [(0, grid[0].index("S"))]
    visited = set()
    result = 0

    while stack:
        r, c = stack.pop()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if r == rows - 1:
            continue

        if grid[r + 1][c] == ".":
            stack.append((r + 1, c))
        elif grid[r + 1][c] == "^":
            result += 1

            if c - 1 >= 0:
                stack.append((r + 1, c - 1))
            if c + 1 < cols:
                stack.append((r + 1, c + 1))

    return result


run_input(day=7, task=1, solution=solution)
