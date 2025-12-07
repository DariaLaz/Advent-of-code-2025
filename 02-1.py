from collections import defaultdict
from main import run_input

known = defaultdict(tuple[int, list])


def invalid_ids_in_range(start, end):
    i = start
    res = []

    while i <= end:
        if i in known:
            if known[i][0] < end:
                res.extend(known[i][1])
                i = known[i][0]
            else:
                k = 0
                while known[i][1][k] < end:
                    res.append(known[i][1][k])
                break
        else:
            string = str(i)

            if string[:len(string) // 2] == string[len(string) // 2:]:
                res.append(i)
        i += 1

    if start not in known or known[start][0] < end:
        known[i] = (end, res)

    return res


def solution(intervals):
    result = 0
    for start, end in intervals:
        result += sum(invalid_ids_in_range(int(start), int(end)))

    return result


run_input(day=2, task=1, solution=solution, split=",",
          process_line=lambda x: x.split("-"))
