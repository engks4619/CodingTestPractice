def solution(n):
    if n <= 1:
        return n
    d = [0 for _ in range(100001)]
    d[0] = 0
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-2] + d[i-1]
    return d[n] % 1234567