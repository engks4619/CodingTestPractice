import math
def solution(fees, records):
    dict = {}
    in_outs = []
    for record in records:
        tmp = record.split(" ")
        in_outs.append(tmp)
        if tmp[1] not in dict:
            dict[tmp[1]] = 0    
    for car in dict.keys():
        st = []        
        for in_out in in_outs:
            if in_out[1] == car and in_out[2] == "IN":
                st.append(in_out[0])
            if in_out[1] == car and in_out[2] == "OUT":
                in_time = st.pop()
                out_time = in_out[0]
                in_tmp = in_time.split(":")
                out_tmp = out_time.split(":")
                in_time = int(in_tmp[0])*60 + int(in_tmp[1])
                out_time = int(out_tmp[0])*60 + int(out_tmp[1])
                time = out_time - in_time
                dict[car] += time
        if st:
            out_time = 1439
            in_time = st.pop()
            in_tmp = in_time.split(":")
            in_time = int(in_tmp[0])*60 + int(in_tmp[1])
            time = out_time - in_time
            dict[car] += time

    default_time = fees[0]
    default_cost = fees[1]
    unit_time = fees[2]
    unit_cost = fees[3]
    for key in dict:
        time = dict[key]
        if time <= default_time:
            dict[key] = default_cost
        else:
            dict[key] = default_cost + math.ceil((time - default_time) / unit_time) * unit_cost
    dict = sorted(dict.items())  
    answer = []
    for i in dict:
        answer.append(i[1])  
    return answer
solution([180, 5000, 10, 600],
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])