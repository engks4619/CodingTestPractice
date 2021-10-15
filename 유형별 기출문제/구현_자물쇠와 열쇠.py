def rotate_90(key):
    n = len(key)
    new_key = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            new_key[x][n-1-y] = key[y][x]
    return new_key

def check(new_lock):
    n = len(new_lock) // 3
    for y in range(n, n*2):
        for x in range(n, n*2):
            if new_lock[y][x] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for y in range(n):
        for x in range(n):
            new_lock[y + n][x + n] = lock[y][x]
    for _ in range(4):
        key = rotate_90(key)
        for y in range(n * 2):
            for x in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[y + i][x + j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[y+i][x+j] -= key[i][j]
    return False

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])