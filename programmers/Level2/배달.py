import heapq
def solution(N, road, K):
    INF = int(1e9)
    distance = [INF for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for i in road:
        start, end, d = i[0], i[1], i[2]
        graph[start].append((end,d))
        graph[end].append((start,d))
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return len([d for d in distance if d <= K])
    
solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)