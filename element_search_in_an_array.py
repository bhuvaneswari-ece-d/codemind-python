n=int(input())
a=list(map(int,input().strip().split()))[:n]
c=int(input())
if c in a:
    print("True")
else:
    print("False")