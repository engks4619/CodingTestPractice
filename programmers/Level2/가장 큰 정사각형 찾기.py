def solution(board):
    row = len(board)
    col = len(board[0])
    sum_board = 0
    
    for i in range(row):
        sum_board += sum(board[i])
    if not sum_board:
        return 0  
              
    max_value = 1
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_value = max(max_value, board[i][j])
    answer = max_value ** 2
    return answer

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])