for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = []
    for i in range(n):
        s, r = map(int, input().split())
        if s<= x:
            arr.append(r)
    print(max(arr))