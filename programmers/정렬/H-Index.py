def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0

print(solution([3,0,6,1,5]))
print(solution([2]))
print(solution([22,42]))