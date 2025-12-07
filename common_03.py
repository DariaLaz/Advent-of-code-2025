def largest(num_str: str, k: int) -> int:
    to_remove = len(num_str) - k
    stack = []

    for num in num_str:
        while to_remove > 0 and stack and stack[-1] < num:
            stack.pop()
            to_remove -= 1

        stack.append(num)

    if to_remove > 0:
        stack = stack[:-to_remove]

    return int("".join(stack))


def common_solution(input, k):
    return sum(largest(num, k=k) for num in input)
