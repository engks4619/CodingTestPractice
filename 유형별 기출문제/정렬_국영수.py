n = int(input())
scoreboard = []
for _ in range(n):
    name, korean_score, english_score, math_score = input().split()
    scoreboard.append([name,int(korean_score),int(english_score),int(math_score)])
scoreboard.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for data in scoreboard:
    print(data[0])