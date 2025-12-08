from common import run_input


def solution(input):
    result = list(map(int, input[0]))
    n = len(result)

    for row in input[1:-1]:
        for col in range(n):
            num = int(row[col])
            if input[-1][col] == '*':
                result[col] *= num
            else:
                result[col] += num

    return sum(result)


run_input(day=6, task=1, solution=solution,
          process_line=lambda x: list(map(lambda y: y.strip(), x.split())))
