def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]
solution([4,3,2,1])
solution([10])