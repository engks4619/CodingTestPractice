def solution(n):
    answer = [int(i) for i in reversed(str(n))]
    answer = list(map(int,list(str(n))[::-1]))
    return answer
solution(12345)