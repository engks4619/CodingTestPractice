def solution(s):
    answer = ""
    s = s.split(" ")
    for c in s:
        if c:
            c = c[0].upper() + c[1:].lower()
        answer += c + " " 
    return answer[:-1]
solution("3people   unFollowed me")
solution("for the last week")