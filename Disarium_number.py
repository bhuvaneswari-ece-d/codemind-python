n=input()
l=len(n)
s=0
for i in range(0,l):
    x=n[i]
    y=(i+1)
    z=int(x)**int(y)
    s+=z
if int(n)==s:
    print("True")
else:
    print("False")