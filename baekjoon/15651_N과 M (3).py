from itertools import product
n, m = map(int,input().split())
for d in list(product([*range(1, n+1)], repeat = m)):
    print(*d)