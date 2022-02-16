for _ in range(int(input())):
    n, p, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    c = 0
    for i in range(p):
        if arr[i] == 0:
            c += x
        else:
            c += y
    print(c)