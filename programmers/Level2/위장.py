from collections import defaultdict
def solution(clothes):
    answer = 0
    dic = defaultdict(list)
    for cloth in clothes:
        dic[cloth[1]].append(cloth[0])   
    tmp = 1
    for key in dic.keys():
        tmp *= (len(dic[key])+1)
    answer = tmp-1
    return answer
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])