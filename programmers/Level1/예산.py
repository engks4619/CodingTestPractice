def solution(d, budget):
    answer = 0
    d.sort()
    for a in d:
        if budget >= a:
            budget -= a
            answer += 1
        else:
            break
    return answer