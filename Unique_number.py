n=input()
l=list(n)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        continue
if l==l1:
    print("Unique Number")
else:
    print("Not Unique Number")