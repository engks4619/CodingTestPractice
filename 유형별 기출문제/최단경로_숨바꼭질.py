import heapq
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
start = 1
q = [(0, start)]
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q,(cost,i))
max_dist = max(distance[1:])
print(distance.index(max_dist), max_dist, distance.count(max_dist))

