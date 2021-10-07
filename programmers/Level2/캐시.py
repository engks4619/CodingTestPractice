def solution(cacheSize, cities):
    answer = 0
    st = []
    for city in cities:
        city = city.lower()
        if city not in st:
            st.append(city)
            answer += 5
            if len(st) > cacheSize:
                st.pop(0)
        else:
            st.remove(city)
            st.append(city)
            answer += 1
    return answer

solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"])