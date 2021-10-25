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

g = int(input())
parent = [i for i in range(g+1)]
p = int(input())
count = 0
infos = []
for _ in range(p):
    infos.append(int(input()))
for info in infos:
    v = find_parent(parent, info)
    if v == 0:
        break
    union_parent(parent, v, v-1)
    count += 1
print(count)
