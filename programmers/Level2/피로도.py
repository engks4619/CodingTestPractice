from itertools import permutations
def solution(k, dungeons):
    answer = -1    
    for candiates in permutations(dungeons,len(dungeons)):
        pirodo = k
        count = 0
        for candi in candiates:
            if candi[0] <= pirodo:
                pirodo -= candi[1]
                count += 1
        answer = max(answer, count)
    return answer

solution(80,[[80,20],[50,40],[30,10]])