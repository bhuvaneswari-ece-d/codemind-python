n=int(input())
a=list(map(int,input().strip().split()))[:n]
s=0
for i in range(len(a)):
    s+=a[i]
if s//n in a:
    print("True")
else:
    print("False")