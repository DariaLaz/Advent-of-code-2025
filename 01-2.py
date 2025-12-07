from main import run_input


def solution(input):
    score = 50
    count = 0

    for ins in input:
        direction = ins[0]
        delta = int(ins[1:]) if direction == "R" else -int(ins[1:])

        new_score = (score + delta) % 100

        if delta > 0:
            count += (score + delta) // 100
        else:
            count += (((100 - score) % 100) + (-delta)) // 100

        score = new_score

    return count


run_input(day=1, task=2, solution=solution)
