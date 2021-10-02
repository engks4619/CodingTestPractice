def solution(rows, columns, queries):
    arr = [[0]*columns for _ in range(rows)]
    answer = []
    count = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = count
            count += 1       
    for query in queries:
        ny1, nx1, ny2, nx2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1  
        min_value = rows * columns 
        tmp1 = arr[ny1][nx1]
        for nx in range(nx1, nx2):
            tmp2 = arr[ny1][nx+1]
            arr[ny1][nx+1] = tmp1
            tmp1 = tmp2
            min_value = min(min_value, tmp1)      
        for ny in range(ny1, ny2):
            tmp2 = arr[ny+1][nx2]
            arr[ny+1][nx2] = tmp1
            tmp1 = tmp2
            min_value = min(min_value,tmp1)
        for nx in range(nx2, nx1, -1):
            tmp2 = arr[ny2][nx-1]
            arr[ny2][nx-1] = tmp1
            tmp1 = tmp2
            min_value = min(min_value,tmp1)
        for ny in range(ny2, ny1, -1): 
            tmp2 = arr[ny-1][nx1]
            arr[ny-1][nx1] = tmp1
            tmp1 = tmp2
            min_value = min(min_value,tmp1)
        answer.append(min_value)
    return answer
solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])