def solution(word):
    dic = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    nums = []
    answer = 0
    prev = 0
    for i in range(5):
        tmp = 5 ** i
        nums.append(prev + tmp)
        prev += tmp
    nums = sorted(nums,reverse=True)
    for idx, w in enumerate(word):
        answer += dic[w] * (nums[idx]) + 1
    print(answer)
    return answer
solution("AAAE")