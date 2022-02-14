for _ in range(int(input())):
    n,k = map(int, input().split())
    if k == 0:
        print(n)
        continue
    print(n-(int(n/k)*k))