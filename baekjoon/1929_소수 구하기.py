#M 이상 N이하의 소수 구하기
import math
M, N = map(int,input().split())
array = [True for _ in range(1000001)]
array[1] = False
for i in range(2, int(math.sqrt(N))+1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1
for i in range(M, N+1):
    if array[i]:
        print(i)