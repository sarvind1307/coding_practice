for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    c = d = b[0]
    for i in range(1, a):
        if(c == 0):
            break
        c -= 1
        c += b[i]
        d += b[i]
    print(d)
