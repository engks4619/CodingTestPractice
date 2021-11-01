import heapq
n = int(input())
graph = [[] for _ in range(n+1)]
def dijkstra(start):
    q = []
    INF = int(1e9)
    heapq.heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))