for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = set(map(int, input().split()))
    if len(arr) >= m:
        print("No")
    else:
        print("Yes")