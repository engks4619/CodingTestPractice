'''
def solution(land):
    n = len(land)
    for i in range(0, n-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])  
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])    
    print(land)     
    return max(land[n-1])
'''
def solution(land):
    n = len(land)
    for i in range(n-1):
        for j in range(len(land[0])):
            land[i+1][j] += max(land[i][:j] + land[i][j+1:])       
    return max(land[n-1])
solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])