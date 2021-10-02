def solution(tickets):
    answer = []
    T = dict()
    for t in tickets:
        if t[0] in T:
            T[t[0]].append(t[1])
        else:
            T[t[0]]= [t[1]]
    for i in T.keys():
        T[i].sort(reverse=True)  
    stack = ["ICN"]
    while stack:
        city = stack[-1]
        if city not in T or len(T[city]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(T[city][-1])
            T[city].pop()

    answer.reverse()
    return answer
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])