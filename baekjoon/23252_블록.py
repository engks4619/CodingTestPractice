import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int,input().split())
    if a >= c and (a+c) % 2 == 0:
        if (b % 2 != 0 and a != 0) or b % 2 == 0:
            print("Yes")
            continue
    print("No")