import heapq
import sys
input = sys.stdin.readline
v, e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
INF = int(1e9)
distance = [INF] * (v+1)
for _ in range(e):
    a, b, dist = map(int,input().split())
    graph[a].append((b, dist))
q = [(0,start)]
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
for d in distance[1:]:
    print(d if d != INF else "INF")