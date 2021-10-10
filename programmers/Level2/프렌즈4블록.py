def solution(m, n, board):
    board = [list(c) for c in board]
    answer = 0
    remove_set = set()
    while True:
        remove_set.clear()
        for y in range(m):
            for x in range(n):
                check_four(x,y,board,remove_set)
        board, answer = organize_block(remove_set,board,answer)
        if not remove_set:    
            return answer

def check_four(x,y,board,remove_set):
    if not board[y][x]:
        return
    if 0 <= y + 1 < len(board) and 0 < x + 1 < len(board[0]):
        if board[y][x] and (board[y+1][x] == board[y][x+1] == board[y+1][x+1] == board[y][x]):
            remove_set.add((y,x))
            remove_set.add((y+1,x)) 
            remove_set.add((y,x+1))
            remove_set.add((y+1,x+1))

def organize_block(remove_set,board,answer):
    for (y, x) in remove_set:
        board[y][x] = None
        answer += 1
    for x in range(len(board[0])):
        for y in range(len(board)-1,-1,-1):
            if board[y][x] == None:
                for k in range(y-1,-1,-1):
                    if board[k][x] != None:
                        board[y][x] = board[k][x]
                        board[k][x] = None
                        break
    return board, answer

solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	)