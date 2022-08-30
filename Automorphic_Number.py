n=int(input())
sq=n**2
d=len(str(n))
c=sq%(pow(10,d))
if n==c:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")