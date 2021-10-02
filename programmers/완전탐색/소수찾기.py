from itertools import permutations
import math
def check_prime(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    if n%2 == 0:
        return True if n==2 else False
    for i in range(2,int(k)+1):
        if n%i == 0:
            return False    
    return True
def solution(numbers):
    answer = 0
    caselist = []
    prime_list = []
    for i in range(1,len(numbers)+1):
        tmp = permutations(numbers,i)
        for j in tmp:
            caselist.append(int("".join(j)))
    caselist = set(caselist)
    for num in caselist:
        if check_prime(num):
            prime_list.append(num)  
    answer = len(prime_list)
    return answer
solution("17")
solution("011")    