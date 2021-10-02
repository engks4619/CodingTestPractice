def isCorrect(s):
    st = []
    dic = {'[':']','{':'}','(':')'}
    for ch in s:
        if ch in list(dic.keys()):
            st.append(ch)
        else:
            if st:
                x = st.pop()
            else:
                return False
            if ch == dic[x]:
                continue
            else:
                return False
    return True
            
def solution(s):
    if len(s) % 2 != 0:
        return 0
    answer = 0
    tmp = ""
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if isCorrect(tmp):
            answer += 1
    return answer

solution("[](){}")
solution("}]()[{")
solution("[)(]")
solution("}}}")
