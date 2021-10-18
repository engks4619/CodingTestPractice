from itertools import combinations
n, m = map(int,input().split())
chicken = []
house = []
for r in range(n):
    data = list(map(int,input().split()))
    for c, d in enumerate(data):
        if d == 1:
            house.append((r,c))
        if d == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))
answer = 1e9
for candidate in candidates:
    result = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(cx-hx)+abs(cy-hy))
        result += tmp
    answer = min(answer, result)
print(answer)