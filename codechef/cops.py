for i in range(int(input())):
    lis=list(range(1,101))
    lis=set(lis)
    m,x,y=map(int,input().split())
    l=list(map(int,input().split()))
    house=[]
    dis=x*y
    for i in l:
        x1=max(1,i-dis)
        x2=min(100,i+dis)
        l1=list(range(x1,x2+1))
        house.extend(l1)
    s=set(house)
    print(len(lis.difference(s)))