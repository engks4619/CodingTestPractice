import heapq
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dummies = []
for _ in range(m):
    k = int(input())
    st = list(map(int,input().split()))
    heapq.heappush(dummies,deque(st[::-1]))
flag = True
number = 1
while number < n:
    dummy = heapq.heappop(dummies)
    if dummy.popleft() == number:
        number += 1
        if dummy:
            heapq.heappush(dummies,dummy)
    else:
        flag = False
        break 
print("Yes" if flag else "No")