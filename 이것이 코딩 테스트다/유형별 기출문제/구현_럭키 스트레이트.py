n = input()
length = len(n)
a, b = list(map(int,n[:length//2])), list(map(int,n[length//2:]))
if sum(a) == sum(b):
    print("LUCKY")
else:
    print("READY")