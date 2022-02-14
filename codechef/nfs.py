for _ in range(int(input())):
    u, v, a, s = map(int, input().split())
    if u == v:
        print("Yes")
    else:
        x = u**2 - 2*a*s
        if x <= v**2:
            print("Yes")
        else:
            print("No")