def calculate_area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def main():
    red_coordinates = []
    with open('input.txt') as f:
        for line in f:
            stripped = line.strip()
            x_str, y_str = stripped.split(",")
            red_coordinates.append((int(x_str), int(y_str)))

    max_area = 0

    for i in range(len(red_coordinates) - 1):
        x1, y1 = red_coordinates[i]
        for j in range(i + 1, len(red_coordinates)):
            x2, y2 = red_coordinates[j]
            area = calculate_area(x1, y1, x2, y2)
            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == "__main__":
    main()
