def solution(n):
    answer = ''
    arr = ["수","박"]
    for i in range(n):
        answer += arr[i%len(arr)]    
    return answer