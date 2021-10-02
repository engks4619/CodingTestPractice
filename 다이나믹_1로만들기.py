import sys
from collections import deque
x = int(sys.stdin.readline())
d = [0 for _ in range(x+1)]
q = deque()
q.append(x)
while q:
    n = q.popleft()
    if n == 1:
        break
    if n % 5 == 0:
        if d[n//5] == 0:
            d[n//5] = d[n] + 1
            q.append(n//5)
    if n % 3 == 0:
        if d[n//3] == 0:
            d[n//3] = d[n] + 1
            q.append(n//3)
    if n % 2 == 0:
        if d[n//2] == 0:
            d[n//2] = d[n] + 1
            q.append(n//2)
    if d[n-1] == 0:
        d[n-1] = d[n] + 1
        q.append(n-1)
        
print(d[1]) 
