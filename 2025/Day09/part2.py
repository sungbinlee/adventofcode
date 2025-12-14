def calculate_area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def compress(values):
    values = sorted(set(values))
    index = {v: i for i, v in enumerate(values)}
    return values, index


def build_polygon_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append((x1, y1, x2, y2))
    return edges


def point_inside_polygon(px, py, edges):
    # ray casting (horizontal ray to +x)
    crossings = 0
    for x1, y1, x2, y2 in edges:
        if y1 == y2:
            continue
        if not (min(y1, y2) < py <= max(y1, y2)):
            continue
        x_at_y = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
        if x_at_y > px:
            crossings += 1
    return crossings % 2 == 1


def main():
    red_coordinates = []
    with open("input.txt") as f:
        for line in f:
            stripped = line.strip()
            x_str, y_str = stripped.split(",")
            red_coordinates.append((int(x_str), int(y_str)))

    edges = build_polygon_edges(red_coordinates)

    xs = []
    ys = []
    for x, y in red_coordinates:
        xs.extend([x, x + 1])
        ys.extend([y, y + 1])

    xs, x_index = compress(xs)
    ys, y_index = compress(ys)

    w = len(xs)
    h = len(ys)

    inside = [[False] * w for _ in range(h)]

    for iy in range(h - 1):
        for ix in range(w - 1):
            cx = (xs[ix] + xs[ix + 1]) / 2
            cy = (ys[iy] + ys[iy + 1]) / 2
            inside[iy][ix] = point_inside_polygon(cx, cy, edges)

    prefix = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(h):
        for x in range(w):
            blocked = 0 if inside[y][x] else 1
            prefix[y + 1][x + 1] = (
                blocked
                + prefix[y][x + 1]
                + prefix[y + 1][x]
                - prefix[y][x]
            )

    max_area = 0
    n = len(red_coordinates)

    for i in range(n - 1):
        x1, y1 = red_coordinates[i]
        for j in range(i + 1, n):
            x2, y2 = red_coordinates[j]

            lx = min(x_index[x1], x_index[x2])
            rx = max(x_index[x1], x_index[x2])
            ty = min(y_index[y1], y_index[y2])
            by = max(y_index[y1], y_index[y2])

            blocked = (
                prefix[by + 1][rx + 1]
                - prefix[ty][rx + 1]
                - prefix[by + 1][lx]
                + prefix[ty][lx]
            )

            if blocked == 0:
                area = calculate_area(x1, y1, x2, y2)
                max_area = max(max_area, area)

    print(max_area)


if __name__ == "__main__":
    main()
