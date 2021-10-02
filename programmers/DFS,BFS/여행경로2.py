def solution(tickets):
    answer = []
    tickets.sort(key = lambda x : x[1])
    stack = ['ICN']
    visited = [False for _ in range(len(tickets))]
    start_city_list = []
    for ticket in tickets:
        start_city_list.append(ticket[0])
    while stack:
        start_city = stack.pop()
        answer.append(start_city)     
         
        for i, ticket in enumerate(tickets):
            if ticket[0] == start_city and visited[i] == False:
                if ticket[1] in start_city_list:
                    visited[i] = True
                    start_city_list.remove(ticket[1])
                    stack.append(ticket[1])
                    break
                else:
                    continue
    for i, v in enumerate(visited):
        if v == False:
            answer.append(tickets[i][1])      
    return answer

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))