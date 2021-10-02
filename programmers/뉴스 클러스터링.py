import string
from collections import Counter    
def solution(str1, str2):    
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    for i in range(len(str1)-1):
        if str1[i] in string.ascii_lowercase and str1[i+1] in string.ascii_lowercase:
            a.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i] in string.ascii_lowercase and str2[i+1] in string.ascii_lowercase:
            b.append(str2[i:i+2])       
    counter1 = Counter(a)
    counter2 = Counter(b)
    hap = list((counter1|counter2).elements())
    gyo = list((counter1&counter2).elements())
    if len(hap) == 0:
        return 65536 
    answer = len(gyo)/len(hap)
    return int(answer * 65536)