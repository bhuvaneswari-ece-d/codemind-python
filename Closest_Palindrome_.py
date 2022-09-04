n=int(input())
s=str(n)
l=[]
l1=[]
for i in range(100,2*n):
    x=str(i)
    x1=list(x)
    y=x1[::-1]
    if x1==y:
         if i<n:
             l.append(i)
         elif i==y:
            continue
         elif i>n:
            l1.append(i)
i=max(l)-n
y=n-min(l1)
if i>y:
    print(max(l))
elif i<y:
    print(min(l1))
else:
    print(max(l),min(l1))