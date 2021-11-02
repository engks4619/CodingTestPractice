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
n = int(input())
parent = [i for i in range(n+1)]
p_x, p_y, p_z = [], [], []
for i in range(1, n+1):
    x, y, z = map(int,input().split())
    p_x.append((x,i))
    p_y.append((y,i))
    p_z.append((z,i))
p_x.sort()
p_y.sort()
p_z.sort()
edges = []
for i in range(n-1):
    edges.append((p_x[i+1][0]-p_x[i][0], p_x[i][1], p_x[i+1][1]))
    edges.append((p_y[i+1][0]-p_y[i][0], p_y[i][1], p_y[i+1][1]))
    edges.append((p_z[i+1][0]-p_z[i][0], p_z[i][1], p_z[i+1][1]))
edges.sort()
cost = 0
for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])
        cost += edge[0]
print(cost)