def check_adjacent_rolls(grid: list, r: int, c: int) -> int:
    H = len(grid)
    W = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    cnt = 0
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < H and 0 <= nc < W:
            if grid[nr][nc] == '@':
                cnt += 1
    return cnt


def count_accessible_rolls(grid: list) -> int:
    H = len(grid)
    W = len(grid[0])

    total = 0

    for r in range(H):
        for c in range(W):
            if grid[r][c] != '@':
                continue

            adj = check_adjacent_rolls(grid, r, c)
            if adj < 4:
                total += 1

    return total


def main():
    grid = []
    with open("input.txt") as f:
        for line in f:
            row = line.strip()
            grid.append(list(row))

    answer = count_accessible_rolls(grid)
    print(answer)


if __name__ == '__main__':
    main()
