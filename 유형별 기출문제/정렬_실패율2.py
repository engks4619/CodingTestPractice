from collections import Counter
def solution(N, stages):
    people = len(stages)
    counter = Counter(stages)
    result = []
    for key in range(1, N+1):
        try:
            result.append((counter[key]/people, key))
            people -= counter[key]
        except:
            result.append((0,key))      
    result.sort(key = lambda x: (-x[0], x[1]))
    answer = [i[1] for i in result]
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4,4,4,4,4])