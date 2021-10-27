def solution(L, x):
    answer = []
    for idx, v in enumerate(L):
        if v == x:
            answer.append(idx)
    return answer if answer else [-1]
solution([64, 72, 83, 72, 54], 72)