from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        time = 0
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
    return answer
solution([1, 2, 3, 2, 3])