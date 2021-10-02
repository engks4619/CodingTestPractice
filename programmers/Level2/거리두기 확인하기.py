def solution(places):
    answer = []
    dx = [1, -1, 0, 0, 2, -2, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 0, 0, 2, -2, 1, -1, 1, -1]    
    for place in places:
        flag = 1
        for i in range(5):
            if not flag:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    for n in range(4):
                        nx = j + dx[n]
                        ny = i + dy[n]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[ny][nx] == "P":
                                flag = 0
                                break
                    for n in range(4, 8):
                        nx = j + dx[n]
                        ny = i + dy[n]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[ny][nx] == "P":
                                if place[(ny+i)//2][(nx+j)//2] != "X":
                                    flag = 0
                                    break
                    for n in range(8, 12):
                        nx = j + dx[n]
                        ny = i + dy[n]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[ny][nx] == "P":
                                if place[i][nx] != "X" or place[ny][j] != "X":
                                    flag = 0
                                    break
        answer.append(flag)
    print(answer)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
   ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])