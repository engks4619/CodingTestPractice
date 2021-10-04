def convert(s):
    data = []
    for c in s:
        if c == "#":
            data[-1] = data[-1].lower()
        else:
            data.append(c)            
    return data
    
def solution(m, musicinfos):
    answer = "(None)"    
    played = {}
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(",")
        start_time = int(musicinfo[0].split(":")[0]) * 60 + int(musicinfo[0].split(":")[1])
        end_time = int(musicinfo[1].split(":")[0]) * 60 + int(musicinfo[1].split(":")[1])
        time = end_time - start_time
        name = musicinfo[2]
        data = convert(musicinfo[3])
        temp = []
        for i in range(time):
            temp.append(data[i % len(data)])
        played[name] = "".join(temp)    
    search_list = convert(m)
    search = "".join(search_list)
    max_len = 0
    for k, v in played.items():
        if search in v and len(v) > max_len:
            max_len = len(v)
            answer = k
    return answer

solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("ABC",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])