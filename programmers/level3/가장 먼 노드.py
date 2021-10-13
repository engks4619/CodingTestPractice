from collections import deque
def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    q = deque()
    q.append(1)
    distance[0] = 0
    distance[1] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            cost = distance[now] + 1
            if distance[i] > cost:
                distance[i] = cost
                q.append(i)
    print(distance)
    return answer
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])