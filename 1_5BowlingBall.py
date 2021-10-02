import time
def selectBall():    
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    start_time = time.time()
    count = 0
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if data[i]!=data[j]:
                count+=1
            else:
                continue

    print (count)    
    end_time = time.time()
    print ("수행시간 :", end_time-start_time)  

selectBall()

      
        
