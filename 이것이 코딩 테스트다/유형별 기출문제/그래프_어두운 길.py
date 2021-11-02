import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b    
n, m = map(int,input().split())
parent = [i for i in range(n)]
edges = []
for _ in range(m):
    a, b, dist = map(int,input().split())
    edges.append((dist, a, b))
edges.sort()
total = 0
result = 0
for edge in edges:
    dist, a, b = edge[0], edge[1], edge[2]
    total += dist
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist
print(total - result)
