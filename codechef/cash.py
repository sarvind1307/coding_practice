for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    r = 0
    print(sum(arr) % k)