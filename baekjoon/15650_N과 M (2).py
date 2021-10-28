from itertools import combinations
n, m = map(int,input().split())
for d in list(combinations([*range(1, n+1)], m)):
    print(*d)