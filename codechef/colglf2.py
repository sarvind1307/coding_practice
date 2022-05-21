for _ in range(int(input())):
    s = int(input())
    q = list(map(int , input().split()))
    t = sum(q)
    for i in range(s):
        l = list(map(int , input().split()))
        t -= l[0]*q[i]
        t += sum(l)-l[0]
    print(t)