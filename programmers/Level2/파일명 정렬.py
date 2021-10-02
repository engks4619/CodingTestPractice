def solution(files):
    answer = []
    temp = []
    for file_number, file in enumerate(files):
        head = ""
        number = ""
        tail = ""
        for i in range(len(file)):
            if file[i].isalpha() or file[i] in ["-"," "]:
                head += file[i]
            else:
                for idx in range(len(file[i:])):
                    if file[i:][idx].isdigit():
                        number += file[i:][idx]
                    else:
                        tail += file[i:][idx:]                
                        break
                break
        temp.append((file_number, head.lower(), int(number), tail))
    temp = sorted(temp, key = lambda x : (x[1], x[2]))
    for t in temp:
        answer.append(files[t[0]])
    return answer
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])