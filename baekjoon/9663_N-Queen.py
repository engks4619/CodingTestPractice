#python3 통과x pypy3 통과
n = int(input())
board = [[0] * n for _ in range(n)]
visited_col = [False] * n
visited_diag1 = [False] * (2 * n - 1)
visited_diag2 = [False] * (2 * n - 1)

def check(r, c):
    if visited_col[c] or visited_diag1[r + c] or visited_diag2[r - c + n - 1]:
        return False
    return True

def dfs(i):  
    global count
    if i == n:
        count += 1
        return
    for j in range(n):
        if check(i, j):
            board[i][j] = 1
            visited_col[j] = True
            visited_diag1[i+j] = True
            visited_diag2[i-j+n-1] = True
            dfs(i+1)
            board[i][j] = 0
            visited_col[j] = False
            visited_diag1[i+j] = False
            visited_diag2[i-j+n-1] = False
count = 0
dfs(0)
print(count)