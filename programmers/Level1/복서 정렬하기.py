def solution(weights, head2head):
    result = []
    for n in range(len(weights)):
        match_count = 0
        win_count = 0
        big_win_count = 0
        for idx,s in enumerate(head2head[n]):
            if s == 'L':
                match_count += 1
            if s == 'W':
                win_count += 1
                if weights[idx] > weights[n]:
                    big_win_count += 1
        win_rate = 0 if win_count + match_count == 0 else win_count / win_count + match_count
        result.append((n+1, win_rate, big_win_count, weights[n]))
    result = sorted(result, key = lambda x : (x[1], x[2], x[3], -x[0]), reverse = True)
    answer = [i[0] for i in result]
    return answer
solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])