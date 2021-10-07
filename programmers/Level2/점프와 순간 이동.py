'''
# bottom-up 방식으로 풀려고 했으나 효율성 통과 X
def solution(n):
    d = [1000000001 for _ in range(n+1)]
    d[0] = 0
    d[1] = 1      
    for i in range(2,n+1):     
        if i % 2 == 0:
            d[i] = d[i//2] 
        else: 
            d[i] = d[i-1]+1
    return d[n]
'''
# top-down 방식
def solution(n):
    ans = 0
    while n:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans

solution(5)
solution(8)