from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
board = []
now_size = 2
now_x, now_y = 0, 0
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 9:
            now_x, now_y = i, j
            data[j] = 0
    board.append(data)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[now_x][now_y] = 0
    q = deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] <= now_size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist):
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= board[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist
time = 0
eat_count = 0
while True:
    data = find(bfs())
    if data == None:
        print(time)
        break
    x, y, dist = data[0], data[1], data[2]
    now_x, now_y = x, y
    time += dist
    board[now_x][now_y] = 0
    eat_count += 1
    if eat_count >= now_size:
        now_size += 1
        eat_count = 0