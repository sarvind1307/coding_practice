for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_num = max(arr)
    min_num = min(arr)
    print(max_num - min_num)