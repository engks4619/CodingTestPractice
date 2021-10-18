from itertools import permutations
def solution(n, weak, dist):    
    INF = 1e9
    answer = INF
    length = len(weak)
    weak += [w + n for w in weak]
    dist.sort(reverse=True)
    for p in list(permutations(dist)):
        print(p)

    print(weak)
    return answer

solution(12, [1, 3, 4, 9, 10], [3, 5, 7])