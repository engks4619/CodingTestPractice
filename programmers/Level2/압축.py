def solution(msg):
    answer = []
    dic = {}
    v = 1
    for i in range(ord("A"), ord("Z") + 1):
        dic[chr(i)] = v
        v += 1 
    temp = ""
    while i in range(len(msg)):
        for m in msg[i:]:
            temp += m
            if temp in dic.keys():
                continue
            else:
                w, c = temp[:-1], temp[-1]
                break
        answer.append(dic[w])
        dic[w+c] = v
        v += 1
        print("w:",w,"c:",c)
            
    print(dic)
    return answer
solution("KAKAO")
