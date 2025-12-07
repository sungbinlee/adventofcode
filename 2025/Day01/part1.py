def move(start: int, command: str, size: int = 100) -> int:
    delta = 0
    direction = command[0]
    value = int(command[1:])

    if direction == "L":
        delta = -value
    elif direction == "R":
        delta = value

    return (start + delta) % size


def main():

    start = 50
    answer = 0

    with open("input.txt", encoding="utf-8") as file:
        for line in file:
            cmd = line.strip()
            if not cmd:
                continue

            result = move(start, cmd, size=100)

            if result == 0:
                answer += 1

            start = result

    print(answer)


if __name__ == "__main__":
    main()
