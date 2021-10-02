def solution(number, k):
    answer = ''
    number = list(number)
    newnumber = []
    length = len(number)
    print(number)
    idx = 0
    for i in range(k-1,0,-1):
        data = number[idx+1:-i]
        maxnum = max(data)
        idx = data.index(maxnum)
        newnumber.append(maxnum)
        print("현재 k값:", i,"최대값의 인덱스:",idx,"최대값:",maxnum)
        print(data)

    
    answer = "".join(newnumber)
    print(answer)
    return answer

solution("1924",2) 
solution("1231234",3)
solution("4177252841",4)   