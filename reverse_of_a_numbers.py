s=input()
n=len(s)
for a in range(n,-1,-1):
    s=s[a-1::-1]
    print(s)
    break
