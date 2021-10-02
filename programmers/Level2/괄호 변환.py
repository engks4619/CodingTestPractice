def seperate(s):
    u = ""
    v = ""
    left_count = 0
    right_count = 0
    check_correct = True
    for idx,c in enumerate(s):
        if c == "(":
            u += c
            left_count += 1
        else:
            u += c
            right_count += 1
        if right_count > left_count:
            check_correct = False
        if left_count == right_count:
            v += s[idx+1:]
            break
    return u, v, check_correct

def solution(p):
    if not p:
        return ""
    u, v, check_correct = seperate(p)
    if check_correct:
        return u + solution(v)
    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        for i in u[1:-1]:
            if i == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp

solution("(()())()")
solution(")(")
solution("()))((()")