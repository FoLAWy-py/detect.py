from collections import deque


def find_shortest_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    start_x, start_y = None, None
    end_x, end_y = None, None

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'Y':
                if start_x is None and start_y is None:
                    start_x, start_y = i, j
                else:
                    end_x, end_y = i, j

    if start_x is None or start_y is None or end_x is None or end_y is None:
        print("未找到起始点Y或终止点Y")
        return

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(start_x, start_y, 0)])
    visited = set()
    paths = []

    while queue:
        x, y, steps = queue.popleft()

        if x == end_x and y == end_y:
            # If we reach the end 'Y', add the path to the list
            path = (x, y, steps)
            paths.append(path)
            continue

        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))

    if not paths:
        print("无法从起始点Y到达终止点Y，没有有效路径。")
    else:
        for path in paths:
            x, y, steps = path
            print(f"从Y到Y的最短路径为 {steps} 步")
            print(f"经过的路径为：")
            print_path(matrix, start_x, start_y, x, y)


def print_path(matrix, start_x, start_y, end_x, end_y):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def backtrack(x, y):
        if x == start_x and y == start_y:
            print(f"({x}, {y})")
            return

        for dx, dy in directions:
            prev_x, prev_y = x - dx, y - dy
            if 0 <= prev_x < rows and 0 <= prev_y < cols and matrix[prev_x][prev_y] != 'X':
                backtrack(prev_x, prev_y)
                print(f"({x}, {y})")
                break

    backtrack(end_x, end_y)


matrix = [
    ['Y', 'X', '#', 'X', 'X', 'X', 'X'],
    ['X', 'X', '#', 'X', '#', '#', 'X'],
    ['X', 'X', 'X', 'X', '#', 'X', 'Y'],
    ['X', 'X', 'X', 'X', '#', 'X', 'X']
]


def print_all_coordinates():
    for i in range(0, 4):
        for j in range(0, 7):
            if matrix[i][j] != '.':
                print(f'({i}, {j}): {matrix[i][j]}')


print_all_coordinates()

find_shortest_path(matrix)
