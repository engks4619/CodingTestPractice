def separate(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_correct(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True

def solution(p):
    answer = ''
    if p == "":
        return answer
    idx = separate(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check_correct(u):
        answer = u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for c in u[1:-1]:
            if c == "(":
                answer += ")"
            else:
                answer += "("
    return answer

solution("(()())()")