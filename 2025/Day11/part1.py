def count_paths(
        graph: [str, [str]],
        start: str,
        end: str,
) -> int:
    memo = {}

    def dfs(node: str) -> int:
        if node == end:
            return 1

        if node in memo:
            return memo[node]

        total_paths = 0
        for next_node in graph.get(node, []):
            total_paths += dfs(next_node)

        memo[node] = total_paths
        return total_paths

    return dfs(start)


def main():
    graph = {}
    with open("input.txt") as f:
        for line in f:
            source, targets = line.strip().split(": ")
            graph[source] = targets.split()

    result = count_paths(graph, start="you", end="out")
    print(result)


if __name__ == "__main__":
    main()
