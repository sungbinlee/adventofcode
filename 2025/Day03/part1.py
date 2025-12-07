def large_jortage(bank: list) -> int:
    length = len(bank)
    candidates = []
    for idx, val in enumerate(bank):
        if idx == length - 1:
            break
        candidates.append(val + max(bank[idx + 1:length]))
    return int(max(candidates))


def main():
    answer = 0
    with open("input.txt") as f:
        for line in f:
            bank = list(line.strip())
            answer += large_jortage(bank)
    print(answer)


if __name__ == '__main__':
    main()
