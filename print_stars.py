import sys

#피라미드
print("피라미드의 높이를 입력하세요 : ")
n = int(sys.stdin.readline())
star = 1
space = n - 1
for i in range(n):
  print(" " * space + "*" * star)  
  star += 2
  space -= 1 
