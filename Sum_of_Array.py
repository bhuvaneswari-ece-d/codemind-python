n=int(input())
s=0
a = list(map(int,input().strip().split()))[:n]
for i in range(len(a)):
        s+=a[i]
print(s)
        