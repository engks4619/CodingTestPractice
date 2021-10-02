import string
def solution(new_id):
    usable_list = []
    for letter in string.ascii_letters:
        usable_list.append(letter)
    for i in range(11):
        usable_list.append(str(i))
    usable_list += ['-', '_', '.']
    #1단계
    new_id = new_id.lower()
    #2단계
    tmp = ''
    for letter in new_id:
        if letter in usable_list:
            tmp += letter
    new_id = tmp
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    #4단계
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id.lstrip('.')
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')
    #5단계
    if new_id == '':
        new_id += 'a'
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')
    #7단계
    if len(new_id)<=2:
        tmp = new_id[-1]
        while len(new_id) < 3:
            new_id += tmp
            
    return new_id