   

def solution(n, k):
    if k != 10:
        tmp = ''
        while n > 0:
            n, mod = divmod(n, k)
            tmp += str(mod)
        s = tmp[::-1]
    else:
        s = str(n)
    print(s)
    num_list = []
    for i in s:
        num = ''
        if i != '0':
            num += i
        num_list.append(num)
    print(num_list)
    answer = -1
    return answer
solution(437674, 3)
solution(110011, 10)