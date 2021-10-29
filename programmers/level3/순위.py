from collections import deque
def solution(n, results):    
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    for result in results:
        graph[result[0]][result[1]] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            answer += 1
    return answer
solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])