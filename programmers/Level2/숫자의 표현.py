def solution(n):
    e = 1
    answer = 1
    while(e < n//2 + 2):
        temp = 0
        for i in range(e, n//2 + 2):
            temp += i
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
        e += 1    
    return answer
solution(15)