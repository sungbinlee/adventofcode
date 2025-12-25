def count_paths_with_constraints(
        graph: [str, [str]],
        start: str,
        end: str,
        required_a: str,
        required_b: str,
) -> int:
    memo = {}

    def dfs(
            node: str,
            visited_a: bool,
            visited_b: bool,
    ) -> int:
        if node == required_a:
            visited_a = True
        if node == required_b:
            visited_b = True

        state = (node, visited_a, visited_b)

        if state in memo:
            return memo[state]

        if node == end:
            return 1 if visited_a and visited_b else 0

        total_paths = 0
        for next_node in graph.get(node, []):
            total_paths += dfs(
                next_node,
                visited_a,
                visited_b,
            )

        memo[state] = total_paths
        return total_paths

    return dfs(start, False, False)


def main():
    graph = {}
    with open("input.txt") as f:
        for line in f:
            source, targets = line.strip().split(": ")
            graph[source] = targets.split()

    result = count_paths_with_constraints(
        graph,
        start="svr",
        end="out",
        required_a="dac",
        required_b="fft",
    )

    print(result)


if __name__ == "__main__":
    main()
