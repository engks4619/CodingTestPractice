def solution(s):
    s = s.lower()
    count_p = s.count('p')
    count_y = s.count('y')
    return True if count_p == count_y else False