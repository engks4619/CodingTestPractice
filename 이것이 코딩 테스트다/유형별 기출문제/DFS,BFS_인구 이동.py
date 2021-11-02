from collections import deque
import sys
input = sys.stdin.readline
n, L, R = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x, y, idx):
    pos = [(x,y)]
    q = deque(pos)
    visited[x][y] = idx
    tmp = board[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if L <= abs(board[nx][ny]-board[x][y]) <= R:
                    q.append((nx,ny))
                    visited[nx][ny] = idx
                    pos.append((nx,ny))
                    tmp += board[nx][ny]
                    count += 1
    for i, j in pos:
        board[i][j] = tmp // count

answer = 0
while True:
    visited = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i, j, idx)
                idx += 1
    if idx == n * n:
        break
    answer += 1

print(answer)


