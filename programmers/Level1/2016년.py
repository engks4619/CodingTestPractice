def solution(a, b):
    day = {1:"FRI",2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED",0:"THU"}
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    tmp = sum(month[:a]) + b
    answer = day[tmp % 7]    
    return answer