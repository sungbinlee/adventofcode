def simulation(grid: list[list[str]]) -> int:
    split_time = 0
    height = len(grid)

    start_x = grid[0].index('S')
    start_beam = (start_x, 1)

    cur_stack = [start_beam]

    for i in range(1, height - 2):
        next_stack = []

        while cur_stack:
            cur_x, cur_y = cur_stack.pop()
            is_split, next_beam = check_splitter(grid[i + 1], cur_x, cur_y)

            if is_split:
                split_time += 1

            next_stack.extend(next_beam)

        cur_stack = list(set(next_stack))

    return split_time


def check_splitter(next_row: list, x: int, y: int) -> tuple:
    next_y = y + 1

    if next_row[x] == "^":
        return True, [(x - 1, next_y), (x + 1, next_y)]

    return False, [(x, next_y)]


def main():
    grid = []
    with open("input.txt") as f:
        for line in f:
            row = line.strip()
            grid.append(list(row))

    print(simulation(grid))


if __name__ == "__main__":
    main()
