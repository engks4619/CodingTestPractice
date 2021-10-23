import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
distance = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    distance[a][b] = min(distance[a][b], c)
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            distance[i][j] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        print(distance[i][j] if distance[i][j] != INF else 0, end = " ") 
    print("")