def move(start: int, command: str, size: int = 100) -> tuple[int, int]:
    direction = command[0]
    steps = int(command[1:])
    zero_count = 0
    position = start

    for _ in range(steps):
        if direction == "L":
            position = (position - 1) % size
        elif direction == "R":
            position = (position + 1) % size

        if position == 0:
            zero_count += 1
    return position, zero_count


def main():
    answer = 0
    start = 50

    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            pos, answer_count = move(start, line, 100)
            start = pos
            answer += answer_count

    print(answer)


if __name__ == "__main__":
    main()
