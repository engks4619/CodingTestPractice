import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())

shark_board = []
for i in range(n):
    shark_board.append(list(map(int,input().split())))
smell_board = [[[0, 0]] * n for _ in range(n)]
directions = list(map(int,input().split()))
priorities = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priorities[i].append(list(map(int,input().split())))

def update_smell_board():
    for i in range(n):
        for j in range(n):
            if smell_board[i][j][1] > 0:
                smell_board[i][j][1] -= 1
                if smell_board[i][j][1] == 0:
                    smell_board[i][j][0] = 0
            if shark_board[i][j] != 0:
                smell_board[i][j] = [shark_board[i][j] , k]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
   
def move_shark():
    new_board = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if shark_board[x][y] != 0:
                find = False
                shark_number = shark_board[x][y]
                direction = directions[shark_number-1]
                for i in range(4):
                    nx = x + dx[priorities[shark_number-1][direction-1][i]-1]
                    ny = y + dy[priorities[shark_number-1][direction-1][i]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell_board[nx][ny][0] == 0:
                            directions[shark_number-1] = priorities[shark_number-1][direction-1][i]
                            if new_board[nx][ny] == 0:
                                new_board[nx][ny] = shark_number
                            else:
                                new_board[nx][ny] = min(new_board[nx][ny], shark_number)
                            find = True
                            break
                if not find:
                    for i in range(4):
                        nx = x + dx[priorities[shark_number-1][direction-1][i]-1]
                        ny = y + dy[priorities[shark_number-1][direction-1][i]-1]
                        if 0 <= nx < n and 0 <= ny < n:
                            if smell_board[nx][ny][0] == shark_number:
                                directions[shark_number-1] = priorities[shark_number-1][direction-1][i]
                                new_board[nx][ny] = shark_number
                                break
    return new_board
time = 0
while True:
    update_smell_board()
    shark_board = move_shark()
    time += 1
    max_shark = 0
    for i in range(n):
        for j in range(n):
            max_shark = max(max_shark, shark_board[i][j])
    if max_shark == 1:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break