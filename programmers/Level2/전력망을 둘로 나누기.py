def solution(n, wires):
    answer = n
    tree = [set() for _ in range(n+1)]    
    for a, b in wires:
        tree[a].add(b)
        tree[b].add(a)
    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        result = abs(2*dfs(a,tree,n) - n)
        answer = min(answer,result)
        tree[a].add(b)
        tree[b].add(a)
    return answer

def dfs(start, tree, n):
    st = [start]
    visited = [False for _ in range(n+1)]
    visited[start] = True
    count = 1
    while st:
        v = st.pop()
        for w in tree[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True 
                count += 1
    return count
solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
