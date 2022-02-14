for _ in range(int(input())):
    a,b,c,d,k = map(int,input().split())
    steps = abs(a-c) + abs(b-d)
    # print(steps)
    if steps == k:
        print("YES")
    elif steps < k and k % 2 == steps % 2:
        print("YES")
    else:
        print("NO")
    