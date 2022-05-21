def user_input():
    arr = []
    for i in range(int(input())):
        arr.append(list(map(int, input().split())))
    print(i, arr)
    
user_input()