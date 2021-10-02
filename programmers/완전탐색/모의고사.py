def solution(answers):
    answer = []
    scorelist = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_score = 0
    b_score = 0
    c_score = 0
    for i in range(len(answers)):
        a_score += 1 if answers[i] == a[i%len(a)] else 0
        b_score += 1 if answers[i] == b[i%len(b)] else 0
        c_score += 1 if answers[i] == c[i%len(c)] else 0
    scorelist = [a_score, b_score, c_score]
    for i, score in enumerate(scorelist):
        if score == max(scorelist):
            answer.append(i+1)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))