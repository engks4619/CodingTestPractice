def solution(name):
    answer = 0  
    vertical = 0  
    horizontal = 0
    change = []
    index = []
    for i,char in enumerate(name):
        if char != 'A':
            change.append(char)
            if i!=0:
                index.append(i)
    if not change:
        return answer
        
    for char in change:    
        vertical += min(ord(char)-ord('A'),ord('Z')-ord(char)+1)   

    right = max(index)
    left = len(name)-min(index)
    rightleft = 20
    
    for i in range(len(index)-1):
        tmp = index[i]*2 + len(name)-index[i+1]
        rightleft = tmp if tmp < rightleft else rightleft
    
    horizontal = min(right,left,rightleft)
    
    answer = vertical+horizontal
    return answer

solution("JEROEN")
solution("JAN")
solution("AAAAA")
solution("ZAAAAZ")
solution("ZAZAAAZ")