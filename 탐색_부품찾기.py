import sys

#순차 탐색
def sequential_search(array_store, array_request):
    print("순차탐색")
    for request in array_request:
        if request in array_store:
            print("yes", end = ' ')
        else:
            print("no", end = ' ')
    print(end = '\n')   

#이진 탐색
def binary_search(array, target, start, end):
    if start > end: 
        return False
    mid = (start + end) // 2
    if array_store[mid] == target:
        return True
    elif array_store[mid] > target:
        return binary_search(array_store,target,start,mid-1) 
    else:
        return binary_search(array_store,target,mid+1,end)
            

n = int(sys.stdin.readline())
array_store = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array_request = list(map(int,sys.stdin.readline().split()))

#순차 탐색
sequential_search(array_store, array_request)

#이진 탐색
print("이진탐색")
for request in array_request:
    if binary_search(array_store,request,0,n-1):
        print("yes", end = ' ')
    else:
        print("no", end = ' ')

#계수 정렬
print(end='\n')
print("계수 정렬")
array = [0]*1000001
for i in array_store:
    array[i] = 1
for request in array_request:
    if array[request]:
        print("yes", end=' ')
    else:
        print("no", end=' ')        
