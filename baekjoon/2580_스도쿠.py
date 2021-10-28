import sys
input = sys.stdin.readline
board = []
empty = []
for i in range(9):
    data = list(map(int,input().split()))
    for j in range(9):
        if data[j] == 0:
            empty.append((i, j))
    board.append(data)

def get_candidates(x, y):
    numbers = [*(range(1,10))]
    for k in range(9):
        if board[x][k] in numbers:
            numbers.remove(board[x][k])
        if board[k][y] in numbers:
            numbers.remove(board[k][y])
    for i in range((x//3) * 3, (x//3) * 3 + 3):
        for j in range((y//3) * 3, (y//3) * 3 + 3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    return numbers

def dfs(count):
    if count == len(empty):
        for b in board:
            print(*b)
        exit(0)
    i, j = empty[count]
    numbers = get_candidates(i, j)
    for num in numbers:
        board[i][j] = num
        dfs(count + 1)
        board[i][j] = 0
dfs(0)