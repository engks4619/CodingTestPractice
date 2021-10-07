def solution(s):
    bin_count, zero_count = 0, 0
    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]        
        bin_count += 1
    return [bin_count,zero_count]

solution("110010101001")