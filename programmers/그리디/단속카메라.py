def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[0], reverse=True)   
    now = routes[0][0]
    for i in routes[1:]:
        if i[1] >= now:
            continue
        else:
            now = i[0]
            answer += 1
    
    return answer
   

print(solution([[0,1], [1,2], [2,3] ,[3,4], [4,5], [5,6], [6,7] , [8,7], [8,9] ,[9,10], [10,11], [11,12], [12,13], [13,14] , [14,15] ])) #8
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))#2
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0]])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-7,0], [-6,-4], [-5,-3], [-3,-1], [-1,4], [1,2], [3,4]]))  #4
print(solution([[-5,-3], [-4,0], [-4,-2], [-1, 2], [0,3], [1,5], [2,4] ])) #2
print(solution([[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]))#2