def solution(board, skill):
    answer = 0
    for s in skill:
        type = s[0]
        x1, y1, x2, y2 = s[1], s[2], s[3], s[4]
        size = s[5]
        if type == 1:
            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    board[j][i] -= size        
        elif type == 2:
            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    board[j][i] += size
    count = 0
    for b in board:
        for i in b:
            if i > 0:
                count += 1
    return count
solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])