def solution(L, x):
    if x not in L:
        print([-1])
        return [-1]
    answer = []
    idx = 0
    while True:
        if x in L:
            idx = L.index(x)
            L = L[idx+1:]
            answer.append(idx)
            print(idx)
        else:
            print(answer)
            return answer
solution([64, 72, 83, 72, 54], 72)