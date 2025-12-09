import math


def main():
    with open("input.txt") as f:
        first_line = f.readline().split()
        problems = [[] for _ in range(len(first_line))]
        operators = []

        for idx, col in enumerate(first_line):
            if not col.isdigit():
                operators.append(col)
            else:
                problems[idx].append(int(col))

        for line in f:
            row = line.split()
            for idx, col in enumerate(row):
                if not col.isdigit():
                    operators.append(col)
                else:
                    problems[idx].append(int(col))

        answer = 0
        for idx, op in enumerate(operators):
            if op == "+":
                answer += sum(problems[idx])
            elif op == "*":
                answer += math.prod(problems[idx])

        print(answer)

if __name__ == '__main__':
    main()
