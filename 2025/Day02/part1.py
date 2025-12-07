def check_invalid_id(start: int, end: int) -> int:
    invalid_id = 0
    for i in range(start, end+1):
        str_id = str(i)
        mid = len(str_id) // 2
        left, right = str_id[:mid], str_id[mid:]
        if left == right:
            invalid_id += int(left + right)

    return invalid_id


def main():
    with open("input.txt", encoding="utf-8") as file:
        sequences = file.readline().split(',')
        answer = 0
        for sequence in sequences:
            start, end = sequence.split('-')
            result = check_invalid_id(int(start), int(end))
            answer += result
        print(answer)


if __name__ == '__main__':
    main()
