import heapq
n, m, start = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))
q = []
heapq.heappush(q,(0,start))
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
count = 0
time = 0
for d in distance:
    if d != INF:
        count += 1
        time = max(time, d)
print(count-1,time)

