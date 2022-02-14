for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    x1 = min(a, b)
    b -= x1
    x2 = min(b, c)
    b -= x2
    if x1 + x2 >= n:
        print("YES")
    else:
        print("NO")
