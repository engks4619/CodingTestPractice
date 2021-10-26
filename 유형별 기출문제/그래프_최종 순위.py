import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    data = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    for _ in range(int(input())):
        a, b = map(int,input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    cycle = False
    duplicate = False
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            duplicate = True
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:                
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif duplicate:
        print("?")
    else:
        print(*result)
