n=int(input())
np=n
pp=n
while True:
    fc=0
    for i in range(1,np+1):
        if np%i==0:
            fc+=1
    if fc==2:
            break
    np+=1
while True:
    fc=0
    for i in range(1,pp+1):
        if pp%i==0:
            fc+=1
    if fc==2:
            break
    pp-=1
x=n-pp
y=np-n
if x<y:
            print(x)
else:
            print(y)