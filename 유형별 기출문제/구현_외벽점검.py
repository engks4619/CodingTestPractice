from itertools import permutations
def solution(n, weak, dist): 
    answer = 1e9
    length = len(weak)
    new_weak = weak + [w + n for w in weak]
    for i in range(length):
        for dists in list(permutations(dist)):
            count = 0
            pos = weak[i]
            for d in dists:
                count += 1
                pos += d
                if pos < new_weak[i + length - 1]:
                    pos = [w for w in new_weak if w > pos][0]
                else:
                    answer = min(answer, count)
    return answer if answer != 1e9 else -1

solution(12, [1, 3, 4, 9, 10], [3, 5, 7])