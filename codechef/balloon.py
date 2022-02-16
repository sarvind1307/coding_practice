for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    brr = []
    for i in range(len(arr)):
        if arr[i] in range(1,8):
            brr.append(arr[i])
            if len(brr) == 7:
                break
    print(i+1)