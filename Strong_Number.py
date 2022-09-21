import math
n=int(input())
s=0
for i in str(n):
    x=math.factorial(int(i))
    s+=x
if s==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")
