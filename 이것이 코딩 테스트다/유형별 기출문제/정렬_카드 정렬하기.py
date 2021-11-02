import heapq
import sys
input = sys.stdin.readline
n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards,int(input()))
result = 0
for _ in range(n-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a + b
    heapq.heappush(cards, a+b)
print(result)
