from collections import deque

def bfs(computers, com, visited):
    queue = deque()
    queue.append(com)
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in range(len(computers)):
            if i != v and computers[v][i] == 1:
                if visited[i] == False:
                    queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(computers, i, visited)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))