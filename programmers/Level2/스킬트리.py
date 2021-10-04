def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill_dict = {}
    for i in range(len(skill)):
        skill_dict[skill[i]] = i
    for skill_tree in skill_trees:
        flag = 0
        for c in skill_tree:
            if c in skill_dict.keys():
                if skill_dict[c] != flag:
                    answer -=1
                    break
                else:
                    flag += 1
    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])