'''
# 순열
from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
operator_count = list(map(int,input().split()))
operator = ["+", "-", "*", "//"]
opers = []
for i in range(len(operator)):
    for _ in range(operator_count[i]):
        opers.append(operator[i])
max_value = -1e9
min_value = 1e9

for p in permutations(opers):
    result = numbers[0]
    for i in range(1, n):
        op = p[i-1]
        if op == "+":
            result += numbers[i]
        elif op == "-":
            result -= numbers[i]
        elif op == "*":
            result *= numbers[i]
        elif op == "//":
            if result < 0:
                result = (result * -1 // numbers[i]) * -1
            else:
                result = result // numbers[i]
    max_value = max(max_value,result)
    min_value = min(min_value,result)    
print(max_value)
print(min_value)
'''
# DFS
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
operator_count = list(map(int,input().split()))

max_value = -1e9
min_value = 1e9

def dfs(i, result):
    global max_value, min_value, operator_count
    if i == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        if operator_count[0] > 0:
            operator_count[0] -= 1
            dfs(i+1, result + numbers[i])
            operator_count[0] += 1
        if operator_count[1] > 0:
            operator_count[1] -= 1
            dfs(i+1, result - numbers[i])
            operator_count[1] += 1
        if operator_count[2] > 0:
            operator_count[2] -= 1
            dfs(i+1, result * numbers[i])
            operator_count[2] += 1
        if operator_count[3] > 0:
            operator_count[3] -= 1
            dfs(i+1, int(result / numbers[i]))
            operator_count[3] += 1

dfs(1,numbers[0])
print(max_value)
print(min_value)