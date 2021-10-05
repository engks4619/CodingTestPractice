def solution(arr):
    def divide(x, y, n):
        if n == 1:
            return [0,1] if arr[y][x] == 1 else [1,0]
        lu = divide(y, x, n//2)
        ru = divide(y, x + n//2, n//2)
        ld = divide(y + n//2, x, n//2)
        rd = divide(y + n//2, x + n//2, n//2)

        if lu == ru == ld == rd == [0,1] or lu == ru == ld == rd == [1,0]:
            return lu
        else:
            return list(map(sum,zip(lu,ru,ld,rd)))
    answer = divide(0, 0, len(arr))
    return answer
solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
