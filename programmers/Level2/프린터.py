from collections import deque
def solution(priorities, location):
    answer = []
    num_list = deque()
    for idx, p  in enumerate(priorities):
        num_list.append((idx, p))
    while(num_list):
        J = num_list.popleft()
        max_p = 0
        for p in num_list:
            max_p = max(p[1],max_p)
        if J[1] < max_p:
            num_list.append(J)
        else:
            answer.append(J)
            continue
    for i in answer:
        if i[0] == location:
            return answer.index(i) + 1

solution([1, 1, 9, 1, 1, 1],0)