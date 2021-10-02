def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    new_numbers = list()
    for i, number in enumerate(numbers):
        if len(number)==1:
            new_numbers.append([number*12, i])
        elif len(number)==2:
            new_numbers.append([number*6, i])
        elif len(number)==3:
            new_numbers.append([number*4, i])
        elif len(number)==4:
            new_numbers.append([number*3, i])
    new_numbers.sort(key = lambda x : x[0], reverse=True)   
    for idx in new_numbers:   
        answer += "".join(numbers[idx[1]])
    if int(answer) == 0:
        return "0"      
    return answer
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))