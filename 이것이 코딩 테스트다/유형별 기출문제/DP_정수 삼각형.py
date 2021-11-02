'''
# 백준
import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
for i in range(n-2, -1, -1):
    for j in range(i+1):
        array[i][j] += max(array[i+1][j], array[i+1][j+1])
print(array[0][0])
'''
# 프로그래머스
def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]