n, m, k = map(int, input().split())
c = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    total_mins = sum(arr[:-1])
    if arr[-1] <= 10 and total_mins >= m:
        c += 1
print(c)