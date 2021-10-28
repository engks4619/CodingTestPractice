from itertools import combinations
l, c = map(int,input().split())
data = list(input().split())
result = []
mo_list = ["a","e","i","o","u"]
for s in combinations(data, l):
    mo_count = 0
    ja_count = 0
    for c in s:
        if c in mo_list:
            mo_count += 1
        else:
            ja_count += 1
    if mo_count >= 1 and ja_count >= 2:
        result.append("".join(sorted(list(s))))
for s in sorted(result):
    print(s)