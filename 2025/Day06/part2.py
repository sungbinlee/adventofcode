import math


def main():
    with open("input.txt") as f:
        lines = [list(line.rstrip("\n")) for line in f]

    width = max(len(row) for row in lines)
    for row in lines:
        row += [" "] * (width - len(row))

    problems = []
    operators = []

    for col in range(width - 1, -1, -1):
        column_chars = [lines[r][col] for r in range(len(lines))]
        operator = column_chars[-1]

        nums = []
        digits = []
        for ch in column_chars[:-1]:
            if ch.isdigit():
                digits.append(ch)
            else:
                if digits:
                    nums.append(int("".join(digits)))
                    digits = []

        if digits:
            nums.append(int("".join(digits)))

        problems.append(nums)
        operators.append(operator)

    answer = 0
    cur_nums = []
    for nums, op in zip(problems, operators):
        if nums:
            cur_num = int("".join(map(str, nums)))
            cur_nums.append(cur_num)
        if op == "+":
            answer += sum(cur_nums)
            cur_nums = []
        elif op == "*":
            answer += math.prod(cur_nums)
            cur_nums = []

    print(answer)


if __name__ == '__main__':
    main()
