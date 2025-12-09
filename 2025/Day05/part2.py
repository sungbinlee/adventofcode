def main():
    ranges = []

    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    blank_index = lines.index("")

    range_lines = lines[:blank_index]

    for line in range_lines:
        if "-" in line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))

    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))
    answer = sum(end - start + 1 for start, end in merged)
    print(answer)

if __name__ == '__main__':
    main()
