from common import run_input


def solution(coordinates):
    coordinates.sort(key=lambda x: x[0])

    result = -1

    for i, c in enumerate(coordinates):
        x1, y1 = c
        for x2, y2 in coordinates[i + 1:]:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            result = max(area, result)

    return result


run_input(day=9, task=1, solution=solution,
          process_line=lambda x: tuple(map(int, x.split(","))))
