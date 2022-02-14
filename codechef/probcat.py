for _ in range(int(input())):
    n = int(input())
    if n in range(1,100):
        print("Easy")
    elif n in range(100, 200):
        print("Medium")
    else:
        print("Hard")