def main():
    answer = 0
    ranges = []
    numbers = []

    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    blank_index = lines.index("")

    range_lines = lines[:blank_index]
    numbers_lines = lines[blank_index+1:]

    for line in range_lines:
        if "-" in line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))

    for line in numbers_lines:
        if line.isdigit():
            numbers.append(int(line))

    for num in numbers:
        inside = any(start <= num <= end for start, end in ranges)
        if inside:
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
