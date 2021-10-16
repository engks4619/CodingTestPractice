def solution(n, times):
    answer = 0
    low = 0
    high = max(times) * n
    while low <= high:
        mid = (low + high) // 2
        result = 0
        for time in times:
            result += mid // time
        if result >= n:
            answer = mid
            high = mid - 1
        elif result < n:
            low = mid + 1
    return answer
solution(6,[7,10])