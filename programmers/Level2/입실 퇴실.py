from collections import deque
def solution(enter, leave):
    answer = [0] * (len(enter)+1)
    tmp = []
    enter = deque(enter)
    leave = deque(leave)
    e = enter.popleft()
    l = leave.popleft()
    while(leave):
        if l in tmp:            
            tmp.remove(l)
            l = leave.popleft()
        else:        
            for i in tmp:
                answer[i] += 1
            answer[e] = len(tmp)
            tmp.append(e)
            if enter :
                e = enter.popleft()
    return answer[1:] 
solution([1,4,2,3],[2,1,3,4])