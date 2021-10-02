from typing import DefaultDict
from collections import Counter
def solution(id_list, report, k):
    dict = DefaultDict(list)
    for r in report:
        tmp = r.split(" ")
        if tmp[1] not in dict[tmp[0]]:
            dict[tmp[0]].append(tmp[1])
    report_list = []
    ban_list = []
    for i in dict.values():
        report_list += i  
    counter = Counter(report_list) 
    
    for f in counter:
        if counter[f] >= k:            
            ban_list.append(f)

    result = {}
    for id in id_list:
        result[id] = 0
    for ban_id in ban_list:
        for key in dict.keys():
            if ban_id in dict[key]:
                result[key] += 1
    answer = list(result.values())
    print(answer)
    return answer
solution(["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)