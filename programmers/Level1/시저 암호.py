def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer += chr(ord(i) + n) if ord('a') <= ord(i) + n <= ord('z') else chr(ord('a') + (ord(i)+n - ord('z')-1))
        elif i.isupper():
            answer += chr(ord(i) + n) if ord('A') <= ord(i) + n <= ord('Z') else chr(ord('A') + (ord(i)+n - ord('Z')-1))
        else:
            answer += i
    return answer
solution("AB",1)