from collections import deque
def check(word1, word2):
    count = 0 
    length = len(word1)
    for i in range(length):
        if word1[i] == word2[i]:
            count += 1
    return True if count == length - 1 else False        


def solution(begin, target, words):
    answer = 0 
    if target not in words or begin == target:
        return answer
    queue = deque()
    for w in words:
        if check(begin, w):
            queue.append([w, 1])
    while queue:
        word, count = queue.popleft()
        if word == target:
            answer = count
            return answer
        for w in words:
            if check(word, w):
                queue.append([w,count+1])
    return answer
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
