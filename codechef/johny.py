# Uncle Johny

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    x = arr[k-1]
    arr.sort()
    print(arr.index(x) + 1)