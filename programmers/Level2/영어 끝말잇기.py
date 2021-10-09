def solution(n, words):
    word_lst = []
    for idx, word in enumerate(words):
        if word in word_lst or (word_lst and word_lst[-1][-1] != word[0]):
            return [idx % n + 1, idx // n + 1]     
        else:
            word_lst.append(word)
    return [0,0]

solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])