for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr) == n:
        print(100)
    elif sum(arr[:m]) == m:
        print(k)
    else:
        print(0)