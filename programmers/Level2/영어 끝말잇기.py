def solution(n, words):
    count_dic = {i: 0 for i in range(1,n+1)}
    word_lst = []
    for idx, word in enumerate(words):
        if word in word_lst:
            return [idx % n + 1, count_dic[idx % n + 1] + 1]     
        else:
            if word_lst and word_lst[-1][-1] != word[0]:
                return [idx % n + 1, count_dic[idx % n + 1] + 1]   
            else:
                word_lst.append(word)
                count_dic[idx % n + 1] += 1
    return [0,0]

solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])