def solution(n, arr1, arr2):
    answer = []
    board = []
    for a1, a2 in zip(arr1, arr2):        
        board.append(bin(a1|a2)[2:].zfill(n))
    for e in board:  
        tmp = ""     
        for i in e:
            tmp += "#" if int(i) else " "
        answer.append(tmp)
    return answer
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))