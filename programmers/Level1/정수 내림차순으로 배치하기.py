def solution(n):
    answer = int(''.join(sorted(str(n),reverse = True)))
    print(answer)
    return answer
solution(118372)