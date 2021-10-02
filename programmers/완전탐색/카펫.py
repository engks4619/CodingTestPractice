def solution(brown, yellow):
    a = 3
    w = 3
    b = 3
    while True:
        b = brown/2 -a + 2
        if (a-2)*(b-2) == yellow:
            w = int(a) if a >= b else int(b)
            h = int(b) if b <= a else int(a)
            break
        a += 1
    answer = [w, h]
    print(answer)
    return answer
solution(10,2)
solution(8,1)
solution(24,24)