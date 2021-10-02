from itertools import combinations
def make_all_case(relation):
    case_list = []
    col = len(relation[0])
    for i in range(1, col + 1):
        case_list.extend(combinations(range(col),i))    
    return case_list

def filter_unique(lst, relation):
    unique_list = []
    for i in lst:
        tmp_list = []
        for r in relation:
            tmp = []
            for idx in i:
                tmp.append(r[idx])
            tmp_list.append(tuple(tmp))
        if len(set(tmp_list)) == len(relation):
            unique_list.append(i)
    return unique_list

def filter_minimal(lst):
    minimal_list = set(lst)
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if set(lst[i]) == set(lst[i]) & set(lst[j]):
                minimal_list.discard(lst[j])
    return minimal_list

def solution(relation):    
    case_list = make_all_case(relation)
    unique_list = filter_unique(case_list, relation)
    candidate_key_list = filter_minimal(unique_list)
    return len(candidate_key_list)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])