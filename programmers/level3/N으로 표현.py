def solution(N, number):
    d = []    
    for i in range(1,9):
        numbers = set()
        numbers.add(int(str(N)*i))
        for j in range(i-1):
            for k in d[j]:
                for l in d[-j-1]:
                    numbers.add(k+l)
                    numbers.add(k-l)
                    numbers.add(k*l)
                    if l != 0:
                        numbers.add(k//l)
        if number in numbers:
            return i
        d.append(numbers)
    return -1

solution(5, 12)