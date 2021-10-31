def solution(gems):
    num_gems = len(set(gems))
    n = len(gems)
    l, r = 0, 0
    gem_dict = {gems[0] : 1}  
    candidate = [1, n]
    while l < n and r < n:
        if len(gem_dict) < num_gems:
            r += 1
            if r >= n:
                break
            if gems[r] in gem_dict.keys():
                gem_dict[gems[r]] += 1
            else:
                gem_dict[gems[r]] = 1
        else:
            if r - l < candidate[1] - candidate[0]:
                candidate = [l+1, r+1]
            if gem_dict[gems[l]]:
                gem_dict[gems[l]] -= 1
                if gem_dict[gems[l]] == 0:
                    del gem_dict[gems[l]]
            l += 1
    return candidate
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])