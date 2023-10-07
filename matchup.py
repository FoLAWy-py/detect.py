
import random

# set gameboard
rows, cols = 8, 13

# initialize gameboard and set icon
board = [['.' for _ in range(cols)] for _ in range(rows)]
icons = [['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
         ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
         ['M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
         ['M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
         ['Y','Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
         ['Y','Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
         ['K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
         ['K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']]

# generate icon randomly
icon_pairs = [icon for row in icons for icon in row]
random.shuffle(icon_pairs)
icon_pairs = icon_pairs[:rows * cols // 2] * 2  # 每个字母图标生成两次
random.shuffle(icon_pairs)

# initialize matrix
for i in range(1, 7):
    for j in range(1, 12):
        board[i][j] = icon_pairs.pop()


# check gameboard
def print_board():
    for row in board[1:7]:
        print(' '.join(row[1:12]))


print_board()


# DFS
def dfs(x1, y1, x2, y2, path=[]):
    # Add the current coordinate to the path
    path.append((x1, y1))

    if x1 == x2 and y1 == y2:
        return True
    
    if (x1 == x2 and y1 == y2 + 1) or (x1 == x2 and y1 == y2 - 1) or (x1 == x2 - 1 and y1 == y2) or (x1 == x2 + 1 and y1 == y2):
          return True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x1 + dx, y1 + dy

        if 1 <= new_x <= 6 and 1 <= new_y <= 11 and board[new_x][new_y] == '.':
            # Check if the new coordinate is in the path
            if (new_x, new_y) not in path:
                # Recursively call dfs with the new coordinate and the updated path
                if dfs(new_x, new_y, x2, y2, path):
                    # Replace matched locations with ' '
                    board[x1][y1] = '.'
                    board[x2][y2] = '.'
                    return True

    # Remove the current coordinate from the path
    path.pop()






# Output directory
def print_all_coordinates():
    for i in range(1, 7):
        for j in range(1, 12):
            if board[i][j] != '.':
                print(f'({i}, {j}): {board[i][j]}')


print_all_coordinates()


# Helper function to check if there is a clear path between two coordinates
def is_path_clear(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True


    if board[x1][y1] != board[x2][y2]:
        return False

    # Use a queue to store the coordinates that need to be visited
    queue = [(x1, y1)]

    # Use a set to store the coordinates that have been visited
    visited = set()

    # Use a loop to explore the adjacent empty spaces
    while queue:
        # Pop the first coordinate from the queue
        x, y = queue.pop(0)

        # Mark it as visited
        visited.add((x, y))

        # Check if it is the target coordinate
        if x == x2 and y == y2:
            return True

        # Check the four directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if the new coordinate is valid and empty
            if 1 <= new_x <= 6 and 1 <= new_y <= 11 and board[new_x][new_y] == '.':
                # Check if it has been visited before
                if (new_x, new_y) not in visited:
                    # Add it to the queue
                    queue.append((new_x, new_y))

    # If the loop ends without finding the target coordinate, return False
    return False






# check if the game is over
def is_game_over():
    for i in range(1, 7):
        for j in range(1, 12):
            if board[i][j] != '.':
                return False
    return True


# __main__
while not is_game_over():
    print("\nCurrentBoard：")
    print_board()

    # input directory
    x1, y1 = map(int, input("请输入第一个字母的坐标（以空格分隔）：").split())
    x2, y2 = map(int, input("请输入第二个字母的坐标（以空格分隔）：").split())

    if 1 <= x1 <= 6 and 1 <= y1 <= 11 and 1 <= x2 <= 6 and 1 <= y2 <= 11:
        if board[x1][y1] == board[x2][y2] and dfs(x1, y1, x2, y2):
            print("成功匹配！")
            board[x1][y1] = '.'
            board[x2][y2] = '.'
        else:
            print("无法匹配。")
    else:
        print("输入的坐标无效，请重新输入。")

print("游戏结束！")