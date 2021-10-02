def solution(s):
    answer = []
    s = s.replace("{{","").replace("}}","").split("},{")
    s.sort(key=len)
    for i in s:
        tmp = i.split(",")
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))
    return answer