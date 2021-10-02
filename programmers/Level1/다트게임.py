import string
def solution(dartResult):
    answer = 0
    SDT = {"S":1, "D":2, "T":3}
    digits = string.digits
    st = []
    tmp = ""
    for i in dartResult:
        if i in digits:
            tmp += i
        else:
            if i in SDT:
                st.append(int(tmp)**SDT[i])
                tmp = ""
            elif i == "*":
                if len(st) >= 2:
                    x = st.pop()
                    y = st.pop()
                    st.append(y*2)
                    st.append(x*2)
                else:
                    x = st.pop()
                    st.append(x*2)
            else:
                x = st.pop()
                st.append(x*-1)
    answer = sum(st)
    return answer

print(solution("1S2D*3T"))