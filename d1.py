for test_case in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    s = 0
    for i in arr:
        if s < i:
            c += 1
            s += 1
            
    print(f"Case #{test_case+1}:", c)