def solution(info, edges):
    dict = {'Sheep' : 1, 'Wolf' : 0}
    cur = 0
    st = []
    visited = [False for _ in range(len(info))]
    while(st):
        for edge in edges:
            if edge[0] == cur and not visited[edge[0]]:
                st.append(edge)
        v = st.pop()  
        print(v)
        sheep = dict['Sheep']   
        wolf = dict['Wolf']        
        if not visited[v[1]]:
            if info[v[1]] == 0:
                sheep += 1
            else:
                wolf += 1                
            if sheep > wolf:
                visited[v[1]] = True
                if info[v[1]] == 0:
                    dict['Sheep'] += 1
                else:
                    dict['Wolf'] += 1 
                cur = v[1]
            else:
                continue
        
    answer = 0
    return answer
solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])