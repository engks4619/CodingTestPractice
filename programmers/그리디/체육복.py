def solution(n, lost, reserve):
    answer = n
    lostList = set(lost) - set(reserve)
    reserveList = set(reserve) - set(lost)
    
    for i in lostList:
        if i-1 in reserveList:
            reserveList.remove(i-1)
        elif i+1 in reserveList:
            reserveList.remove(i+1)
        else:
            answer -= 1
    
    return answer

print(solution(5,[2,4],[1,3,5]))   
print(solution(5,[2,4],[3])) 
print(solution(3,[3],[1]))  
print(solution(10,[5,4,3,2,1],[3,1,2,5,4]))  