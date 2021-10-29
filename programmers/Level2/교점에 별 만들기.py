def solution(line):
    cross_pos = set()
    for i in range(len(line)-1):
        a, b, e = line[i]
        for j in range(i+1, len(line)):            
            c, d, f = line[j]
            if (a*d-b*c):
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x == int(x) and y == int(y):
                    cross_pos.add((int(x), int(y)))
    cross_x = [c[0] for c in cross_pos]
    left, right = min(cross_x), max(cross_x)
    cross_y = [c[1] for c in cross_pos]
    up, down = min(cross_y), max(cross_y)
    board = [["."] * (right - left + 1) for _ in range(down - up + 1)]
    for x, y in cross_pos:
        board[down-y][x-left] = "*"
    answer = ["".join(b) for b in board]
    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])