'''
#bisect 이용
import sys
import bisect
input = sys.stdin.readline
n, x = map(int,input().split())
numbers = list(map(int,input().split()))
left = bisect.bisect_left(numbers,x)
right = bisect.bisect_right(numbers,x)
result = right - left
if result:
    print(result)
else:
    print(-1)
'''
import sys
input = sys.stdin.readline
n, x = map(int,input().split())
numbers = list(map(int,input().split()))
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif target <= array[mid]:
        return first(array, target, start, mid - 1)
    elif target > array[mid]:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif target >= array[mid]:
        return last(array, target, mid + 1, end)
    elif target < array[mid]:
        return last(array, target, start, mid - 1)
a = first(numbers, x, 0, n-1)
b = last(numbers, x, 0, n-1)
if not a :
    print(-1)
else:
    print(b - a +1)