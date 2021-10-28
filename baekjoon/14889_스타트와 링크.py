from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
ablities = []
for _ in range(n):
    ablities.append(list(map(int,input().split())))
candidates = combinations([*range(0, n)], n//2)
result = int(1e9)
for team1 in candidates:
    team2 = [i for i in range(0, n) if i not in team1]
    team1_result = 0
    team2_result = 0
    for team1_tmp in combinations(team1,2):        
        team1_result += ablities[team1_tmp[0]][team1_tmp[1]]
        team1_result += ablities[team1_tmp[1]][team1_tmp[0]]
    for team2_tmp in combinations(team2,2):
        team2_result += ablities[team2_tmp[0]][team2_tmp[1]]
        team2_result += ablities[team2_tmp[1]][team2_tmp[0]]
    result = min(result, abs(team1_result - team2_result))
print(result)