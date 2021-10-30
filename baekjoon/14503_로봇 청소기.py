import sys
input = sys.stdin.readline
n, m = map(int,input().split())
now_x, now_y, direction = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
visited = [[False] * m for _ in range(n)]

def turn_left(direction):
    direction -= 1
    if direction >= 0:
        return direction
    else:
        return 3

def clean(x, y):
    global count
    visited[x][y] = True
    count += 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def find(x, y, direction):
    for _ in range(4):
        direction = turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                return (nx, ny, direction)        
    return None

def go_back(x, y, direction):
    nx = x - dx[direction]
    ny = y - dy[direction]
    if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 0:
            return nx, ny
    return None

count = 0
clean(now_x, now_y)
while True:
    pos = find(now_x, now_y, direction)
    if pos:
        now_x, now_y, direction = pos
        clean(now_x, now_y)
    else:
        back_pos = go_back(now_x, now_y, direction)
        if back_pos:
            now_x, now_y = back_pos
        else:
            print(count)
            break