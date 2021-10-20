from collections import deque
n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
q = deque([x])
distance[x] = 0
while q:
    now = q.popleft()
    for v in graph[now]:
        if distance[v] == -1:
            distance[v] = distance[now] + 1
            q.append(v) 
if k not in distance:
    print(-1)
else:
    for i in range(n+1):
        if distance[i] == k:
            print(i)
