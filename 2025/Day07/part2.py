from collections import defaultdict


def simulation(grid: list[list[str]]) -> int:
    height = len(grid)

    start_x = grid[0].index('S')
    cur_beams = {(start_x, 1): 1}

    for y in range(1, height - 1):
        next_beams = defaultdict(int)

        for (x, cur_y), timeline_count in cur_beams.items():
            is_split, next_positions = check_splitter(grid[y], x, cur_y)

            if is_split:
                for nx, ny in next_positions:
                    next_beams[(nx, ny)] += timeline_count
            else:
                nx, ny = next_positions[0]
                next_beams[(nx, ny)] += timeline_count

        cur_beams = next_beams

    total_timelines = sum(cur_beams.values())
    return total_timelines


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
