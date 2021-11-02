from itertools import combinations
n = int(input())
board = []
teachers = []
empty = []
for i in range(n):
    data = list(map(str, input().split()))
    board.append(data)
    for j in range(n):
        if data[j] == "T":
            teachers.append((i,j))
        elif data[j] == "X":
            empty.append((i,j))
def monitor(i, j, direction):  
    if direction == "U":
        while i < n:
            if board[i][j] == "O":
                return False
            if board[i][j] == "S":
                return True  
            i += 1
    elif direction == "D":
        while 0 <= i:
            if board[i][j] == "O":
                return False
            if board[i][j] == "S":
                return True 
            i -= 1
    elif direction == "L":
        while 0 <= j:
            if board[i][j] == "O":
                return False
            if board[i][j] == "S":
                return True 
            j -= 1
    elif direction == "R":
        while j < n:
            if board[i][j] == "O":
                return False
            if board[i][j] == "S":
                return True
            j += 1
    return False

def look_around():
    for i, j in teachers:
        for direction in ["U","D","L","R"]:
            if monitor(i,j,direction):
                return True
    return False

flag = False
for case in combinations(empty,3):
    for i, j in case:
        board[i][j] = "O"
    for i, j in teachers:        
        if not look_around():
            flag = True
            break
    for i, j in case:
        board[i][j] = "X"
if flag:
    print("YES")
else:
    print("NO")