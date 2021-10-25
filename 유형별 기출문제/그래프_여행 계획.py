import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [i for i in range(n+1)]
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)
plan = list(map(int,input().split()))
group = find_parent(parent, plan[0])
result = True
for i in range(1, m):
    if find_parent(parent, plan[i]) != group:
        result = False
        break
print("YES" if result else "NO")
