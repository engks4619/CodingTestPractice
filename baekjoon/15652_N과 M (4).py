import sys
n, m = map(int,sys.stdin.readline().split())
result = []
def solution(idx):
    if len(result) == m:
        print(*result)
        return
    for i in range(idx, n+1):
        result.append(i)
        solution(i)
        result.pop()
solution(1)