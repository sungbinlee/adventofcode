def check_invalid_id(start: int, end: int) -> int:
    invalid_id = 0

    for i in range(start, end + 1):
        str_id = str(i)
        length = len(str_id)
        found = False

        for step in range(1, length // 2 + 1):

            if length % step != 0:
                continue

            repeat_count = length // step
            pattern = str_id[:step]

            if pattern * repeat_count == str_id:
                invalid_id += i
                found = True
                break

        if found:
            continue

    return invalid_id


def main():
    answer = 0

    with open("input.txt", encoding="utf-8") as file:
        sequences = file.readline().split(',')
        for sequence in sequences:
            start, end = sequence.split('-')
            result = check_invalid_id(int(start), int(end))
            answer += result

    print(answer)


if __name__ == '__main__':
    main()
