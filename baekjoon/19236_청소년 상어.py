from copy import deepcopy
import sys
input = sys.stdin.readline
board = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        board[i][j] = [data[j*2], data[j*2 + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(board, idx):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == idx:
                return (i, j)
    return None
    
def move_fish(board, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(board, i)
        if position != None:
            x, y = position[0], position[1]
            direction = board[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        board[x][y][1] = direction
                        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                        break
                direction = (direction+1) % 8

def get_eatable_positions(board, now_x, now_y):
    direction = board[now_x][now_y][1]
    positions = []
    for _ in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if board[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

result = 0
def dfs(board, now_x, now_y, total):
    global result
    board = deepcopy(board)
    total += board[now_x][now_y][0]
    board[now_x][now_y][0] = -1
    move_fish(board, now_x, now_y)
    positions = get_eatable_positions(board, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return
    for x, y in positions:
        dfs(board, x, y, total)
    
dfs(board,0,0,0)
print(result)