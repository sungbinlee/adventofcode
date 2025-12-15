from collections import deque


def build_target_mask(diagram: str) -> int:
    mask = 0
    for i, ch in enumerate(diagram):
        if ch == "#":
            mask |= 1 << i
    return mask


def build_button_masks(buttons: list[list[int]]) -> list[int]:
    masks = []
    for button in buttons:
        mask = 0
        for idx in button:
            mask |= 1 << idx
        masks.append(mask)
    return masks


def parse_line(line: str):
    target_part = line[line.index("{") + 1: line.index("}")]
    target = [int(x) for x in target_part.split(",")]

    buttons_part = line[line.index("]") + 1: line.index("{")]
    buttons = []
    for token in buttons_part.split():
        if token.startswith("("):
            buttons.append(
                [int(x) for x in token.strip("()").split(",") if x]
            )

    return target, buttons


def bfs_min_presses(target: int, button_masks: list[int]) -> int:
    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        state, presses = queue.popleft()

        if state == target:
            return presses

        for mask in button_masks:
            next_state = state ^ mask
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))


def main():
    answer = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()

            target, buttons = parse_line(line)
            answer += solve_machine(target, buttons)
    print(answer)


if __name__ == "__main__":
    main()
