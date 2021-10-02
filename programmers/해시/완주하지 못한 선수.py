def solution(participant, completion):
    answer = ''
    dic = dict()
    h_value = 0
    for p in participant:
        dic[hash(p)] = p
        h_value += hash(p)
    for c in completion:
        h_value -= hash(c)
    answer = dic[h_value]
    return answer
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))    
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))