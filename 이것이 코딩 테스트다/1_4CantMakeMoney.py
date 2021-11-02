def minMoney():
    n = int(input())
    data = list(map(int,input().split()))
    data.sort()

    target = 1
    for num in data:
        if target<num:
            break
        target+=num
    return target
print(minMoney())    