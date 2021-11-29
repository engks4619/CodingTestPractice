import heapq
import sys

INF = int(1e9)


def dijkstra():
    q = [(0, 0, 0)]
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        cost, x, y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = board[nx][ny] + cost
                if distance[nx][ny] > new_cost:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
    return distance[N-1][N-1]


T = int(input())
input = sys.stdin.readline
for C in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip())))
    print(board)
    print(f"#{C} {dijkstra()}")
