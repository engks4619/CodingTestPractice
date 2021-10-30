from collections import deque
def solution(n):
    if n <= 3:
        return n 
    q = deque([0,1])
    for _ in range(n):
        a = q.popleft()
        b = q[0]
        q.append((a + b) % 1000000007)
    return q[1]