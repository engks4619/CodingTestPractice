import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
b, c = map(int,input().split())
count = 0
for number in numbers:
    number -= b
    if number >= 0:
        count += number // c if number % c == 0 else number // c + 1
    count += 1
print(count)