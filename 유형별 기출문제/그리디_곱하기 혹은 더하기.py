s = list(map(int,input()))
s.sort()
answer = 0
for i in s:
    if i <= 1 or answer == 0:
        answer += i
    else:
        answer *= i
print(answer)