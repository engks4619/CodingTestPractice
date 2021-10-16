import heapq
def solution(jobs):
    answer = 0
    q = []
    jobs.sort()
    n = len(jobs)
    time = 0
    count = 0
    while count < n:
        for job in jobs[:]:
            if job[0] <= time:
                heapq.heappush(q,[job[1],job[0]]) 
                jobs.pop(0)         
        if q:
            work_time, request_time = heapq.heappop(q)
            time += work_time
            answer += time-request_time   
            count += 1
        else:
            time += 1
    return answer // n
solution([[0, 3], [1, 9], [2, 6]])