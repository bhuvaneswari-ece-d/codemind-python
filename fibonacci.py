n=int(input())
l=[0,1]
x=0
y=1
for i in range(0,n):
    z=x+y
    x=y
    y=z
    l.append(z)
    if len(l)==n:
        break
print(*l)
