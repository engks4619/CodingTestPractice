import sys
input = sys.stdin.readline
n = int(input())
t = [0] * n
p = [0] * n
dp = [0] * (n+1)
for i in range(n):
    t[i], p[i] = map(int,input().split())
for i in range(n-1, -1, -1):
    if i + t[i] > n:      
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])  
print(dp)
