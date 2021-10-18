n = int(input())
board = [[None]*(n) for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int,input().split())
    board[r-1][c-1] = "Apple"
l = int(input())
st = []
for _ in range(l):
    x, c = input().split()
    st.append([int(x), c])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = 0
head_x, head_y = 0, 0
board[0][0] = 1
pos = [(head_x, head_y)] 
time = 0
while True:
    nx, ny = head_x + dx[direction], head_y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n and board[ny][nx] != 1:
        if board[ny][nx] == None:
            board[ny][nx] = 1
            pos.append((nx,ny))
            tail_x, tail_y = pos.pop(0)
            board[tail_y][tail_x] = None
        elif board[ny][nx] == "Apple":
            board[ny][nx] = 1
            pos.append((nx,ny))
    else:
        time += 1
        break
    head_x, head_y = nx, ny
    time += 1    
    if st and time == st[0][0]:
        if st[0][1] == "D":
            direction = (direction+1) % 4
        elif st[0][1] == "L":
            direction = (direction-1) % 4   
        st.pop(0) 
print(time)