import heapq

def solution(food_times, k):
    answer = 0
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value+(q[0][0]-previous)*length <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length-=1
        previous = now   

    return answer