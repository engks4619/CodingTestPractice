def solution(s):
    tmp = s.split(" ")
    new = []
    for word in tmp:
        w = ''
        for idx, c in enumerate(word):
            w += c.upper() if idx % 2 == 0 else c.lower()
        new.append(w)
    answer = ' '.join(new)
    return answer
solution("try hello world")