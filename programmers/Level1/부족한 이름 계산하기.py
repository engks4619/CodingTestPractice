def solution(price, money, count):
    cost = 0
    for i in range(1,count+1):
        cost += price*i if 1<= price*i <=2500 else 2500
        print(cost)
    print(cost,money)
    answer = cost - money if cost-money > 0 else 0   
    return answer

solution(3,20,4)