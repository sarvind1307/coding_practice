for _ in range(int(input())):
    l, r = map(int, input().split())
    if l==r:
        print(1)
    elif l<r:
        print((2*r-2*l)+1)
