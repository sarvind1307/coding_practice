for _ in range(int(input())):
    n,s = map(int, input().split())
    x = abs(n-s)
    y = abs(n - x)
    print(y)