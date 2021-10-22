import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    array = [[] for _ in range(n)]
    idx = 0
    for i in range(n):
        array[i] = data[idx:idx + m]
        idx += m
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                array[i][j] += max(array[i][j-1], array[i+1][j-1])
            elif i == n-1:
                array[i][j] += max(array[i-1][j-1], array[i][j-1])
            else:
                array[i][j] += max(array[i-1][j-1], array[i][j-1], array[i+1][j-1])
    answer = 0
    for i in range(n):
        answer = max(answer,array[i][m-1])
    print(answer)