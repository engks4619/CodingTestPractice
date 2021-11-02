def solution(N, stages):
    people = len(stages)
    fail_percentage = []
    for i in range(1, N + 1):
        count = stages.count(i)
        if people > 0:
            fail_percentage.append((count/people,i))  
        else:
            fail_percentage.append((0,i))  
        people -= count
    fail_percentage.sort(key = lambda x: (-x[0], x[1]))
    answer = [i[1] for i in fail_percentage]
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4,4,4,4,4])