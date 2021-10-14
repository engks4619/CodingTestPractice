s = input()
char_list = []
num = 0
for i in s:
    if i.isalpha():
        char_list.append(i)
    else:
        num += int(i)
char_list.sort()
print("".join(char_list)+str(num))