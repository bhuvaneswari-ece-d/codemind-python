s=input()
n=len(s)
for a in range(n,-1,-1):
    u=s[a-1::-1]
    break
v=int(u)
sq=str(v**2)
x=int(s)
sq1=str(x**2)
h=sq1[::-1]
if sq==h:
    print("True")
else:
    print("False")
