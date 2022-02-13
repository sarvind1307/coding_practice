def get_sum(a,b):
    s = 0
    if a < b:
        a,b = b,a
    for i in range(a, b+1):
        print(i)
        s += i
    return s

print(get_sum(0, -1))