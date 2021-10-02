def solution(table, languages, preference):
    result = []
    for i in table:        
        score = 0
        i = i.split(" ")
        for idx,lan in enumerate(languages):
            if lan in i:
                score += preference[idx]*(len(i)-i.index(lan))
        result.append((i[0],score))
    result = sorted(result, key = lambda x : (-x[1],x[0]))  
    return result[0][0]
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["PYTHON", "C++", "SQL"],[7, 5, 5])
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["JAVA", "JAVASCRIPT"],[7, 5])