import math
def solution(n):
    x = math.sqrt(n)
    return int((x+1)**2) if x.is_integer() else -1
solution(121)
solution(3)