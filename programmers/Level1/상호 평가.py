def get_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return  'B'
    elif 70 <= score < 80:
        return 'C'
    elif 50 <= score < 70:
        return 'D'
    else:
        return 'F'
def solution(scores):
    answer = ''
    for num in range(len(scores)):
        s_scores = []
        for i in range(len(scores)):
            s_scores.append(scores[i][num])
        if s_scores[num] == max(s_scores) or min(s_scores):
            if s_scores[num] == max(s_scores) and s_scores.count(max(s_scores)) == 1:
                del s_scores[num]
            elif s_scores[num] == min(s_scores) and s_scores.count(min(s_scores)) == 1:
                del s_scores[num]
        score = sum(s_scores) / len(s_scores)
        answer += get_grade(score)
    return answer
solution([[100,90,98,88,65],[50,45,99,85,77],
[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
solution([[50,90],[50,87]])
solution([[70,49,90],[68,50,38],[73,31,100]])