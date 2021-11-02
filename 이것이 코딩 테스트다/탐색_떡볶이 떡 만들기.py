def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)    
n, m = map(int,input().split())
arr = list(map(int,input().split()))
start = 0
end = max(arr)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for a in arr:
        if a > mid:
            total += a - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid +1
print(result)