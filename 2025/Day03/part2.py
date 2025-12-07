def large_jortage(bank: str) -> int:
    k = 12
    n = len(bank)
    drop = n - k
    stack = []

    for digit in bank:
        while drop > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)

    result = ''.join(stack[:k])
    return int(result)


def main():
    answer = 0
    with open("input.txt") as f:
        for line in f:
            bank = line.strip()
            answer += large_jortage(bank)
    print(answer)


if __name__ == '__main__':
    main()
