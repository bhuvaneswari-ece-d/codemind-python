n=int(input())
l=list(map(int,input().strip().split()))[:n]
c=0
x=int(input())
for i in range(len(l)):
    if l[i]==x in l:
        c+=1
print(c)
