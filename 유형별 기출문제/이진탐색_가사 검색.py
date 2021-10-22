from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    for i in range(10001):
        if array[i]:
            array[i].sort()
        if reversed_array[i]:
            reversed_array[i].sort()
    for word in words:
        n = len(word)
        array[n].append(word)
        reversed_array[n].append(word[::-1])
    for query in queries:
        n = len(query)
        if query[-1] == "?":
            left_value, right_value = query.replace("?","a"), query.replace("?","z")
            left_idx = bisect_left(array[n], left_value)
            right_idx = bisect_right(array[n], right_value)
            answer.append(right_idx - left_idx)
        else:
            left_value, right_value = query.replace("?","a"), query.replace("?","z")
            left_idx = bisect_left(reversed_array[n], left_value)
            right_idx = bisect_right(reversed_array[n], right_value)
            answer.append(right_idx - left_idx)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])