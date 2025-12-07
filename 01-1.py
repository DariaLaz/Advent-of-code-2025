from main import run_input


def solution(input):
    score = 50
    count = 0

    for i in input:
        sign = 1 if i[0] == 'R' else -1
        score += (sign * int(i[1:]))
        score %= 100
        if score == 0:
            count += 1

    return count


run_input(day=1, task=1, solution=solution)
