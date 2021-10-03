def solution(msg):
    answer = []
    dic = {}
    v = 1
    for i in range(ord("A"), ord("Z") + 1):
        dic[chr(i)] = v
        v += 1 
    st = []
    for m in msg:
        st.append(m)
    w = ""
    while st:
        w += st.pop(0)
        c = st[0] if st else ""
        add = w + c
        if add not in dic.keys():
            dic[add] = v
            v += 1
            answer.append(dic[w])
            w = ""
        else:
            continue
    answer.append(dic[w])
    return answer
solution("KAKAO")
