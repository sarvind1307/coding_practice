for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    s += s * c/100
    # print(s)
    if s >= a and s <=b:
        print("Yes")
    else:
        print("No")