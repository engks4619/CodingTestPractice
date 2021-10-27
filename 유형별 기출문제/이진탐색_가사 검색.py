from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    word_sizes = set()
    for word in words:
        word_size = len(word)
        word_sizes.add(word_size)
        array[word_size].append(word)
        reversed_array[word_size].append(word[::-1])    
    for i in word_sizes:
        array[i].sort()
        reversed_array[i].sort()
    for query in queries:
        query_size = len(query)
        if query[0] != "?":  
            left_value, right_value = query.replace("?","a"), query.replace("?","z")          
            left_idx = bisect_left(array[query_size], left_value)
            right_idx = bisect_right(array[query_size], right_value)
            result = right_idx - left_idx
        else:
            left_value, right_value = query[::-1].replace("?","a"), query[::-1].replace("?","z")
            left_idx = bisect_left(reversed_array[query_size], left_value)
            right_idx = bisect_right(reversed_array[query_size], right_value)
            result = right_idx - left_idx
        answer.append(result)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])