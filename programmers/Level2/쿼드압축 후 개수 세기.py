'''
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
'''
def solution(arr):
    answer = [0,0]
    def divide(y, x, n):
        if n == 1:
            answer[arr[y][x]] += 1
            return
        else:
            prev = arr[y][x]
            for dy in range(n):
                for dx in range(n):
                    if prev != arr[y+dy][x+dx]:
                        divide(y, x, n//2)
                        divide(y, x + n//2, n//2)
                        divide(y + n//2, x, n//2)
                        divide(y + n//2, x + n//2, n//2)
                        return
            answer[prev] += 1
    divide(0, 0, len(arr))
    return answer
solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
