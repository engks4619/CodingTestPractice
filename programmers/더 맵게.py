import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    count = 0
    while heap:
        food1 = heapq.heappop(heap)
        if food1 < K:
            if heap:
                food2 = heapq.heappop(heap)
                now_s = food1 + food2 * 2
                count += 1
                heapq.heappush(heap,now_s)
        else:
            return count
    return -1   
print(solution([0, 0, 0, 0, 0, 1],7))