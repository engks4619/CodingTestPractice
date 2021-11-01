import heapq
def solution(operations):
    min_q = []
    max_q = []
    for operation in operations:
        oper = operation[0]
        value = int(operation[2:])
        if oper == "I":
            heapq.heappush(min_q, value)
            heapq.heappush(max_q, -value)
        elif oper == "D" and min_q and max_q:
            if value == 1:
                heapq.heappop(max_q)
                min_q.pop(-1)
            elif value == -1:
                heapq.heappop(min_q)
                max_q.pop(-1)
    answer = [max_q[0] * -1, min_q[0]] if min_q and max_q else [0, 0]
    return answer