def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer
solution([1,4,2],[5,4,4])
solution([1,2],[3,4])