def solution(x):
    y = sum(map(int,str(x)))
    return True if x % y == 0 else False
solution(10)
solution(12)