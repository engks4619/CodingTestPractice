dp_zero = [0] * 41
dp_one = [0] * 41
dp_zero[0], dp_zero[1] = 1, 0
dp_one[0], dp_one[1] = 0, 1
for _ in range(int(input())):
    n = int(input())
    for i in range(2, n+1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]
    print(dp_zero[n], dp_one[n])