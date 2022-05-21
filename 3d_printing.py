for test_case in range(int(input())):
    printer_1 = list(map(int, input().split()))
    printer_2 = list(map(int, input().split()))
    printer_3 = list(map(int, input().split()))
    # C - Cyan M - Megenta Y - Yellow K - black
    arr = []
    for i in range(4):
        arr.append(min(printer_1[i], printer_2[i], printer_3[i]))

    res = []
    t = 1000000
    if sum(arr) < 1000000:
        res.append("IMPOSSIBLE")
    else:
        for i in arr:
            x = min(t, i)
            res.append(x)
            t -= min(t, i)

    print(f"Case #{test_case+1}:", *res)
