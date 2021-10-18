#실패 코드
def solution(n, build_frame):
    result = []
    board = [[None]*(n+1) for _ in range(n+1)]
    for b in build_frame:
        x, y, element, work = b[0], b[1], b[2], b[3]
        if element == 0:
            if work == 1:
                if y == 0:
                    board[y][x] = 0
                elif 0 <= y-1 <= n:
                    if board[y-1][x] == 0:
                        board[y][x] = 0
                if 0 <= x-1 <= n:
                    if board[y][x-1] == 1:
                        board[y][x] = 0
                if 0 <= x+1 <= n:
                    if board[y][x+1] == 1:
                        board[y][x] = 0
            elif work == 0:
                if 0 <= y+1 <= n:
                    if board[y+1][x] == None:
                        board[y][x] = None
                    elif board[y+1][x] == 0:
                        continue
                    elif board[y+1][x] == 1:
                        if 0 <= x-1 <= n and 0 <= x+1 <= n:
                            if board[y+1][x-1] == board[y+1][x+1] == 1:
                                board[y][x] = None
                            else:
                                continue
                else:
                    board[y][x] = None
        elif element == 1:
            if work == 1:
                if 0 <= y-1 <= n:
                    if board[y-1][x] == 0:
                        board[y][x] = 1
                    if 0 <= x+1 <= n:
                        if board[y-1][x+1] == 0:
                            board[y][x] = 1
                if 0 <= x-1 <= n and 0 <= x+1 <= n:
                    if board[y][x-1] == board[y][x+1] == 1:
                        board[y][x] = 1
            elif work == 0: 
                if 0 <= y+1 <= n:
                    if board[y+1][x] == 0:
                        continue
                    if 0 <= x+1 <= n:
                        if board[y+1][x+1] == 0:
                            continue
                if 0 <= x+1 <= n and 0 <= x-1 <= n:
                    if board[y][x-1] == board[y][x+1] == 1:
                        continue
                board[y][x] = None                    
    for y in range(n+1):
        for x in range(n+1):
            if board[y][x] != None:
                result.append([x,y,board[y][x]]) 
    result.sort()             
    return result
solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])