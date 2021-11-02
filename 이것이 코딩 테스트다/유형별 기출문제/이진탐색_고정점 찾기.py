import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))
def find_fixed_point(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == array[mid]:
        return mid
    elif mid < array[mid]:
        return find_fixed_point(array, start, mid - 1)
    else:
        return find_fixed_point(array, mid + 1, end)
    
answer = find_fixed_point(array, 0, n-1)
if answer:
    print(answer)
else:
    print(-1)    