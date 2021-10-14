import heapq
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    n = len(food_times)
    st = []
    for i in range(n):
        st.append((food_times[i], i+1))
    st.sort()
    prev = 0
    for i, food in enumerate(st):
        height = food[0] - prev
        width = n
        if k >= height * width:
            k -= height * width
            prev = food[0]
        else:
            k %= n
            tmp = []
            for i in st[i:]:
                tmp.append(i[1])
            tmp.sort()
            print(tmp[k])
            return tmp[k]
        n -= 1
        
solution([3, 1, 2],5)