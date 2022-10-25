x,y=map(int,input().split())
r=x+2*y
if x==0 and y%2==0:
    print("YES")
elif x==0 and y%2!=0:
    print("NO")
elif r%2==0:
    print("YES")
else:
    print("NO")