from itertools import combinations
def solution(numbers):
    answer = []
    tmp = list(combinations(numbers,2))
    for i in tmp:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer