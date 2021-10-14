"""
n, m = map(int,input().split())
k = list(map(int,input().split()))
count = 0
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i] != k[j]:
            count += 1
print(count)
"""
from collections import Counter
n, m = map(int,input().split())
k = list(map(int,input().split()))
counter = dict(Counter(k))
result = 0
for v in counter.values():
    n -= v
    result += v * n
print(result)
