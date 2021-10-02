def solution(progresses, speeds):
    answer = []
    p_st = list(reversed(progresses))
    s_st = list(reversed(speeds))
    tmp = 0
    while p_st:        
        p = p_st.pop()
        s = s_st.pop()
        day = 0        
        while p < 100:
            p += s
            day += 1
        if day > tmp:
            answer.append(1)
            tmp = day
        else:
            answer[-1] += 1
    return answer