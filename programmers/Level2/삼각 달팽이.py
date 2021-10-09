def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    x, y = -1, 0
    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            arr[y][x] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                answer.append(arr[i][j])
    return answer

solution(4)
solution(5)