def solution(record):
    answer = []
    uid = {}
    for i in record:
        tmp = i.split()
        if len(tmp) == 3:
            id, name = tmp[-2], tmp[-1]
            uid[id] = name
    for i in record:
        tmp = i.split()
        act, id = tmp[0], tmp[1]
        if act == "Enter":
            answer.append(uid[id]+"님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(uid[id]+"님이 나갔습니다.")
        else:
            continue    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))