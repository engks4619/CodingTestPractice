class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    linked_list = [Node() for _ in range(n)]
    for i in range(1, n):
        linked_list[i-1].next = linked_list[i]
        linked_list[i].prev = linked_list[i-1]
    cur = linked_list[k] 
    deleted = []  
    for oper in cmd:
        if oper[0] == "U":
            for _ in range(int(oper[2:])):
                cur = cur.prev
        elif oper[0] == "D":
            for _ in range(int(oper[2:])):
                cur = cur.next
        elif oper[0] == "C":
            deleted.append(cur)
            cur.removed = True
            up = cur.prev
            down = cur.next
            if up:
                up.next = down
            if down:
                down.prev = up
                cur = down
            else:
                cur = up
        elif oper[0] == "Z":
            v = deleted.pop()
            v.removed = False
            up = v.prev
            down = v.next
            if up:
                up.next = v
            if down:
                down.prev = v
    answer = ""
    for i in range(n):
        if linked_list[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])