def solution(n):
    arr = ['1','2','4']
    answer = ''
    while n != 0:
        a, rest = divmod(n-1,3)
        answer += arr[rest]
        n = a      
    return answer[::-1]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))

