def solution(s):
    bin_count = 0
    zero_count = 0
    while True:
        print(s)
        zero_count += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]        
        bin_count += 1
        if s == "1":
            break
    print([bin_count,zero_count])
    return [bin_count,zero_count]

solution("110010101001")