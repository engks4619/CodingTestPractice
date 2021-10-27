def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        tmp = s[:i]
        count = 1
        result = ""
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                count += 1
            else:
                result += str(count) + tmp if count != 1 else tmp
                tmp = s[j:j+i]
                count = 1
        result += str(count) + tmp if count != 1 else tmp
        answer = min(answer,len(result))
    return answer

solution("aabbaccc")