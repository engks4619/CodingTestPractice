import sys
from itertools import combinations
import time
input = sys.stdin.readline

start_time = time.time()
n, m = map(int,input().split())
board = []
tmp_board = [[0] * m for _ in range(n)]
empty = []
virus = []
for i in range(n):
    data = list(map(int,input().split()))
    board.append(data)
    for j, d in enumerate(data):
        if d == 0:
            empty.append((i,j))
        elif d == 2:
            virus.append((i,j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                spread(nx,ny)
def count_safe():
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == 0:
                count += 1
    return count

result = 0
for p in combinations(empty,3):
    for i in range(n):
        for j in range(m):
            tmp_board[i][j] = board[i][j]
    for i, j in p:
        tmp_board[i][j] = 1
    for i, j in virus:
        spread(i,j)
    result = max(result, count_safe()) 
print(result)
