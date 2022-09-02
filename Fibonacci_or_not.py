n=int(input())
l=[]
x=0
y=1
for i in range(0,n//2+1):
    z=x+y
    x=y
    y=z
    l.append(z)
print(n in l)