def possible(answer):
    for x, y, element in answer:
        if element == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        if element == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
def solution(n, build_frame):
    answer = []
    for b in build_frame:
        x, y, element, oper = b
        if oper == 1:
            answer.append([x, y, element])
            if not possible(answer):
                answer.remove([x, y, element])
        if oper == 0:
            answer.remove([x, y, element])
            if not possible(answer):
                answer.append([x, y, element])
    answer.sort(key = lambda x : (x[0], x[1]))
    return answer

solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])