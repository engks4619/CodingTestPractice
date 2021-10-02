from collections import Counter
def solution(N, stages):
    answer = []
    tmp = []
    n = len(stages)
    for i in range(1, N+1):
        if n != 0:
            count = stages.count(i) 
            fail = count / n
            tmp.append((i,fail))
            n -= count
        else:
            tmp.append((i,0))
    tmp.sort(key = lambda x : x[1], reverse = True)    
    
    for i in tmp:
        answer.append(i[0])
    return answer