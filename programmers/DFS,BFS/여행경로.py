from collections import deque
def solution(tickets):
    answer = []
    visited = [0 for _ in range(len(tickets))]    
    startlist = []
    for idx, ticket in enumerate(tickets):
        startlist.append(ticket[0])
    print(startlist)
    queue = deque()
    queue.append("ICN")
    while sum(visited)!=len(tickets):
        start_city = queue.popleft()
        answer.append(start_city)  
        citylist = []      
        for idx, ticket in enumerate(tickets):                  
            if ticket[0] == start_city and visited[idx] == 0:            
                citylist.append([ticket[1], idx])
            citylist.sort()   
        for i in range(len(citylist)): 
            if citylist[i][0] in startlist:
                if visited[citylist[i][1]] == False:
                    destination = citylist[i][0]
                    ticket_num = citylist[i][1]
                    break
        visited[ticket_num] = 1
        queue.append(destination)
    answer.append(tickets[ticket_num][1])   
    print(answer)   
    return answer
solution([["ICN","AAA"],["ICN","BBB"],["BBB","ICN"]])  