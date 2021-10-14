s = input()
tmp1 = [i for i in s.split("1") if i != ""]
tmp2 = [i for i in s.split("0") if i != ""]
print(min(len(tmp1),len(tmp2)))



