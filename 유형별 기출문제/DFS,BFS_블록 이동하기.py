from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def get_next_pos(pos, board):
    n = len(board)
    next_pos = []
    pos = list(pos)
    pos_x1, pos_y1, pos_x2, pos_y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        next_pos_x1, next_pos_y1, next_pos_x2, next_pos_y2 = pos_x1 + dx[i], pos_y1 + dy[i], pos_x2 + dx[i], pos_y2 + dy[i]
        if 0 <= next_pos_x1 < n and 0 <= next_pos_y1 < n and 0 <= next_pos_x2 < n and 0 <= next_pos_y2 < n:         
            if board[next_pos_x1][next_pos_y1] == 0 and board[next_pos_x2][next_pos_y2] == 0:
                next_pos.append({(next_pos_x1,next_pos_y1),(next_pos_x2,next_pos_y2)})    
    for d in [1,-1]:
        if pos_x1 == pos_x2:
            if 0 <= pos_x1 + d < n:
                if board[pos_x1 + d][pos_y1] == 0 and board[pos_x2 + d][pos_y2] == 0:
                    next_pos.append({(pos_x1,pos_y1),(pos_x1+d,pos_y1)})
                    next_pos.append({(pos_x2,pos_y2),(pos_x2+d,pos_y2)})
        if pos_y1 == pos_y2:        
            if 0 <= pos_y1 + d < n:
                if board[pos_x1][pos_y1 + d] == 0 and board[pos_x2][pos_y2 + d] == 0:
                    next_pos.append({(pos_x1,pos_y1),(pos_x1,pos_y1+d)})
                    next_pos.append({(pos_x2,pos_y2),(pos_x2,pos_y2+d)})
    return next_pos

def solution(board):
    n = len(board)
    pos = {(0,0),(0,1)}
    q = deque()
    q.append((pos,0))
    visited = []
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n-1, n-1) in pos:
            return cost        
        next_poses = get_next_pos(pos, board)
        for next_pos in next_poses:
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])