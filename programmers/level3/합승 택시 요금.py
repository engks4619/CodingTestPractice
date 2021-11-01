import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))    
    def dijkstra(start, goal):
        q = []
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
        return distance[goal]
    answer = INF
    for k in range(1, n+1):
        answer = min(answer, dijkstra(s, k) + dijkstra(k, a) + dijkstra(k, b))
    return answer

solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])