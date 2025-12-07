from main import run_input


def largest(line):
    first, second = None, None

    last = 0

    for i, num in enumerate(line):
        if i != len(line) - 1 and (first is None or num > first):
            if first and second:
                last = int(first) * 10 + int(second)
            first = num
            second = None
        elif second is None or num > second:
            second = num

    return last if second is None else int(first) * 10 + int(second)


def solution(input):
    return sum(largest(i) for i in input)


run_input(day=3, task=1, solution=solution)
