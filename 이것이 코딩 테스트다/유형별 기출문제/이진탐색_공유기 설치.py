import sys
input = sys.stdin.readline
n, c = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
start = 1
end = array[-1] - array[0]
answer = -1
while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] - value >= mid:
            count += 1
            value = array[i]
    if count < c:
        end = mid -1
    else:
        answer = mid
        start = mid + 1
print(answer)