import heapq
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    d = [INF for _ in range(N+1)]
    for v in road:
        graph[v[0]].append((v[1],v[2]))
        graph[v[1]].append((v[0],v[2]))
    def dijkstra(start):
        q = []
        d[start] = 0
        heapq.heappush(q,(0,start))
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < d[i[0]]:
                    d[i[0]] = cost
                    heapq.heappush(q, (cost,i[0]))
    dijkstra(1)
    answer = len([i for i in d if i <= K])
    return answer
solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)