import math
import heapq


def distance(a: tuple[int, int, int],
             b: tuple[int, int, int]) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def uf_init(n: int) -> tuple[list[int], list[int]]:
    parent = list(range(n))
    size = [1] * n
    return parent, size


def uf_find(parent: list[int], a: int) -> int:
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


def uf_union(parent: list[int], size: list[int],
             a: int, b: int):
    root_a = uf_find(parent, a)
    root_b = uf_find(parent, b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True


def main():
    points = []
    with open('input.txt') as f:
        for line in f:
            stripped = line.strip()
            x_str, y_str, z_str = stripped.split(",")
            points.append((int(x_str), int(y_str), int(z_str)))

    num_points = len(points)
    num_edges = 1000

    heap = []

    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = distance(points[i], points[j])
            heapq.heappush(heap, (dist, i, j))

    parent, size = uf_init(num_points)
    components = num_points

    last_i = -1
    last_j = -1

    while components > 1 and heap:
        _, i, j = heapq.heappop(heap)
        merged = uf_union(parent, size, i, j)
        if merged:
            components -= 1
            last_i, last_j = i, j

    x1 = points[last_i][0]
    x2 = points[last_j][0]
    result = x1 * x2
    print(result)


if __name__ == "__main__":
    main()
