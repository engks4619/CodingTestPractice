from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        tmp = []
        for order in orders:
            tmp.extend(combinations(sorted(order),i))
        counter = Counter(tmp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))