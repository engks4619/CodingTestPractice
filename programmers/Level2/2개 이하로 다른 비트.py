def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:            
            bit_number = list("0" + bin(number)[2:])
            for i in range(len(bit_number)-1,-1,-1):
                if bit_number[i] == "0":
                    bit_number[i] = "1"
                    bit_number[i+1] = "0"
                    break
            answer.append(int("".join(bit_number),2))
    return answer
solution([2,7])