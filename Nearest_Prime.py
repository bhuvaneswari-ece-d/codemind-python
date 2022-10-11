a=int(input())
for l in range(a):
    n=int(input())
    pre_prime=n
    np=n
    while True:
        fc=0
        for i in range(1,pre_prime+1):
            if pre_prime%i==0:
                fc+=1
        if fc==2:
            break
        pre_prime-=1
    while True:
        fc=0
        for i in range(1,np+1):
            if np%i==0:
                fc+=1
        if fc==2:
            break
        np+=1
    x=n-pre_prime
    y=np-n
    if x<y:
        print(pre_prime)
    elif x>y:
        print(np)
    if x==y:
        print(min(np,pre_prime))
