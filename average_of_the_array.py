n=int(input())
l=list(map(int,input().strip().split()))[:n]
s=0
for i in range(len(l)):
    s+=l[i]
r=s/n
ff="{:.2f}".format(r)
print(ff)