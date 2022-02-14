for _ in range(int(input())):
    n = int(input())
    s = ((n+1)*n)/2
    if s % 2 != 0:
        print(n-1)
    else:
        print(n)
