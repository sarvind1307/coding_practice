for _ in range(int(input())):
    w1, w2, x1, x2, M = map(int, input().split())
    wt = w2 - w1
    min_wt = M * x1
    max_wt = M * x2
    
    if wt in range(min_wt, max_wt+1):
        print(1)
    else:
        print(0)