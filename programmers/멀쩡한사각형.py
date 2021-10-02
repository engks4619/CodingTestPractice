import math
def solution(w,h):
    if w == h:
        answer = w * h - w
    else:
        answer = w * h - (w+h-math.gcd(w,h))
    return answer