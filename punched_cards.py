for i in range(int(input())):
    r, c = map(int, input().split())
    print(f"Case #{i+1}:")
    for i in range(2*r):
        if i == 0:
            print("..", end = "")
            print("+-" * (c - 1), end = "")
            print("+")
        if i == 1:
            print("..", end = "")
            print("|." * (c - 1), end = "")
            print("|")
        elif i != 0 and i % 2 == 0:
            print("+-" * c, end = "")
            print("+")
        elif i != 1 and i % 2 != 0:
            print("|." * c, end = "")
            print("|")
    print("+-" * c,end = "")
    print("+")