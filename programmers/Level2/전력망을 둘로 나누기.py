def solution(n, wires):
    answer = n
    adj = [set() for _ in range(n+1)]    
    for a, b in wires:
        adj[a].add(b)
        adj[b].add(a)
    for a, b in wires:
        adj[a].remove(b)
        adj[b].remove(a)
        result = abs(2*dfs(a,adj,n) - n)
        answer = min(answer,result)
        adj[a].add(b)
        adj[b].add(a)
    return answer

def dfs(start, adj, n):
    st = [start]
    visited = [False for _ in range(n+1)]
    visited[start] = True
    count = 1
    while st:
        v = st.pop()
        for w in adj[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True 
                count += 1
    return count
solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
