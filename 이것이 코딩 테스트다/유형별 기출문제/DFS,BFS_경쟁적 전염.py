import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
board = []
virus = []
for i in range(n):
    data = list(map(int,input().split()))
    for j, d in enumerate(data):
        if d != 0:
            virus.append((d,0,i,j))
    board.append(data)
virus.sort()
q = deque(virus)
second, target_x, target_y = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def spread(num_virus, time, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = num_virus
                q.append((num_virus, time + 1, nx, ny))

while q:
    num_virus, time, x, y = q.popleft()
    if time == second:
        break
    else:
        spread(num_virus, time, x, y)

print(board[target_x-1][target_y-1])


