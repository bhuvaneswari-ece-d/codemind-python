n=int(input())
l=list(map(int,input().strip().split()))[:n]
l1=[]
for i in range(len(l)):
    if l[i]%2!=0:
        l1.append(i)
print(list.pop(l1))