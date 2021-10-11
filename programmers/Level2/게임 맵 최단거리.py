from collections import deque
def solution(maps):
    bfs(0,0,maps)
    answer = maps[-1][-1]
    return answer if answer > 1 else -1
def bfs(x,y,maps):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                if not maps[ny][nx]:
                    continue
                if maps[ny][nx] == 1:
                    maps[ny][nx] += maps[y][x]
                    q.append((nx,ny))

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])