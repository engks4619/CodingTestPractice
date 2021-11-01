from collections import deque
def solution(board):    
    INF = int(1e9)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    def bfs(start):
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = 0
        q = deque([start])
        while q:
            x, y, curr_cost, direction = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    new_cost = curr_cost + 100 if i % 2 == direction % 2 else curr_cost + 600
                    if new_cost < dp[nx][ny]:
                        dp[nx][ny] = new_cost
                        q.append([nx, ny, new_cost, i])                        
        return dp[n-1][n-1]    
    return min([bfs((0, 0, 0, 0)), bfs((0, 0, 0, 1))])
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])