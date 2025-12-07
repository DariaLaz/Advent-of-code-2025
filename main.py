import os

INPUT_DIR = "inputs"
OUTPUT_DIR = "outputs"


def run_input(day: int, task: int, solution, process_line=None):
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = f"{day:02d}-{task}.py"

    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)

    if not os.path.isfile(input_path):
        print(f"No such file {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        input = list(filter(lambda x: x, f.read().split("\n")))

        if process_line:
            input = list(map(process_line, input))

        result = solution(input)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(result))

        print(f"Done")
