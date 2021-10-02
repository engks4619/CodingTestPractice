def solution(board, moves):
    answer = 0
    box = []
    for move in moves:        
        for i in range(len(board)):            
            if board[i][move-1] != 0:
                box.append(board[i][move-1])                
                board[i][move-1] = 0
                break     
        if len(box) >= 2:
            if box[-2] == box[-1]:
                box = box[:-2]
                answer += 2     
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))