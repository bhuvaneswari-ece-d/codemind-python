n=int(input())
e=0
o=0
a = list(map(int,input().strip().split()))[:n]
for i in range(len(a)):
    if i%2==0:
        e+=a[i]
    else:
        o+=a[i]
print(abs(e-o))