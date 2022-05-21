for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 1
    p = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < p:
            p = arr[i]
            c += 1
    print(c)