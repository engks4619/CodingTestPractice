n = int(input())
data = list(map(int,input().split()))
answer = 0
data.sort()
count = 0
for d in data:   
    count += 1 
    if d <= count:
        answer += 1
        count = 0
print(answer)

