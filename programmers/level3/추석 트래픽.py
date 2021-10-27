def get_time(time, duration):
    t = time.split(":")    
    end_time = int(t[0])*60*60*1000 + int(t[1])*60*1000 + int(float(t[2])*1000)
    start_time = int(end_time - float(duration)*1000 + 1)
    return start_time, end_time

def solution(lines):
    answer = 0
    lst = []
    for line in lines:
        start_time, end_time = get_time(line.split()[1],line.split()[2][:-1])
        lst.append((start_time,end_time))
    for i in range(len(lst)):
        left = lst[i][1]
        right = left + 1000
        count = 0
        for j in range(len(lst)):
            s = lst[j][0]
            e = lst[j][1]
            if left <= s < right:
                count += 1
                continue
            if left <= e < right:   
                count += 1
                continue
            if s <= left and right <= e:
                count += 1
                continue
        answer = max(answer, count)
    return answer

solution(
		["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
)