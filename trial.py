

# def MaximumAbsoluteDifference(N, S):
#     freq = {}
#     for i in S:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     x = list(freq.values())
#     y = list(filter(lambda x: x % 2 != 0, x))
#     z = list(filter(lambda x: x % 2 == 0, x))
#     w = max(abs(max(y) - min(z)) , abs(max(z) - min(y)))
#     return w
# x = MaximumAbsoluteDifference(10,"aaaabbc")
# print(x)

# def MaximumAbsoluteDifference(N, S):
#     return 1

# def defeatWinner(votes, candidates):
#     freq = {}
#     for i in votes:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

#     x = list(freq.values())
#     x.sort(reverse = True)
#     if candidates > 2:
#         if x[1] + x[2] > x[0]:
#             return True
#         else:
#             return False
#     else:
#         return False
# x = defeatWinner([1,1,1,1,2,2,3,3,3], 3)
# print(x)

def printResult(n, strlist, check):
    key = [['*', '*', '*', 'Q', 'W', 'E', 'R', 'T'],
           ['Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D'],
           ['F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X'],
           ['C', 'V', 'B', 'N', 'M', '*', '*', '*']]
    l_check = len(check)
    arr = []
    for i in strlist:
        if check == i[0:l_check]:
            arr.append(i[l_check:l_check + 1])
    print(arr)
    for i in range(len(key)):
        for j in range(8):
            if key[i][j] not in arr:
                print('* ',end = '')
            else:
                print("{1} ".format(key[i][j]))
        print("\n")
                    



def main():
    n = int(input())
    strlist = []
    for i in range(n):
        temp = input()
        strlist.append(temp)
    check = input()
    printResult(n, strlist, check)


main()
