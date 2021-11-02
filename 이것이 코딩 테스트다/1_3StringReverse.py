def reverseString():
    data = input()
    countZerotoOne = 0
    countOnetoZero = 0
    if data[0]=='1':
        countOnetoZero+=1
    else:
        countZerotoOne+=1   
    for i in range(len(data)-1):
        if data[i]!=data[i+1]:
            if data[i+1]=='1':
                countOnetoZero+=1
            else:
                countZerotoOne+=1
    return min(countZerotoOne,countOnetoZero)
print(reverseString())

