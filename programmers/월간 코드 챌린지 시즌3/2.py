import time
def solution(n, left, right):
    start_time = time.time()
    arr = []
    for i in range(left//n, n):
        for _ in range(i):
            arr.append(i+1)
        for j in range(i,n):
            arr.append(j+1)
        if len(arr) >= right-left//n:
            break
    print(arr[left-(left//n)*n:right-(left//n)*n+1],time.time()-start_time)
    return arr[left-(left//n)*n:right-(left//n)*n+1]

solution(10**7,7,14)