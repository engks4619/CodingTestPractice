def solution(n):
    count = 0
    for c in bin(n)[2:]:
        count += int(c)
    for i in range(n+1, 1000001):
        tmp_count = 0
        for c in bin(i)[2:]:
            tmp_count += int(c)
        if tmp_count == count:
            return i

'''
def solution(n):
    count = bin(n).count('1')
    for i in range(n+1, 1000001):
        c = bin(i).count('1')
        if c == count:
            return i
'''
solution(78)