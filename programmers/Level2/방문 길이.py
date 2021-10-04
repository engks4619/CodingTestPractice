def solution(dirs):
    direction = {"U": (0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
    route = set()
    pos = (0,0)
    for dir in dirs:
        nx = pos[0] + direction[dir][0]
        ny = pos[1] + direction[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            next = (nx, ny)        
            route.add((pos,next))
            route.add((next,pos))
            pos = next  
    return len(route)//2

solution("ULURRDLLU")
solution("LULLLLLLU")