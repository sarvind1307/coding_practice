n = int(input())
arr = list(map(int, input().split()))
c = 0
m = max(arr)
for i in arr:
    c += m - i
print(c)