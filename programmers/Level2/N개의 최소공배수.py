def solution(arr):
    while(len(arr) >= 2):  
        a = arr.pop()
        b = arr.pop()
        tmp1 = set()
        tmp2 = set()
        for i in range(1,a+1):
            if a % i == 0:
                tmp1.add(i)
        for i in range(1,b+1):
            if b % i == 0:
                tmp2.add(i)
        arr.append(a * b // max(tmp1&tmp2))
    answer = arr.pop()
    return answer