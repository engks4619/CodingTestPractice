def solution(s):    
    if len(s) == 1:
        return 1  
    
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        result = ""
        count = 1
        tmp = s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i] == tmp:
                count += 1
            else:
                result += str(count)+tmp if count != 1 else tmp
                tmp = s[j:j+i]
                count = 1                
        result += str(count)+tmp if count !=1 else tmp
        answer = min(answer,len(result))
    return answer