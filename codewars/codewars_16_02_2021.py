'''
8 kyu
Returning Strings
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
'''
def greet(name):
    x = "Hello, {0} how are you doing today?".format(name)
    return x

'''
8 kyu
Calculate average
Python:
'''
def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# 8 kyu
# Keep Hydrated!
# Python:
def litres(time):
    return time // 2

# 5 kyu
# Moving Zeros To The End
# Python:
def move_zeros(array):
    brr = []
    for i in range(len(array)):
        if array[i] != 0:
            brr.append(array[i])
    brr.extend([0] * (len(array) - len(brr)))
    return brr

# 7 kyu
# String ends with?
# Python:
def solution(string, ending):
    if ending == '':
        return True
    e = len(ending)
    if string[-e:] == ending:
        return True
    else:
        return False
    
# 6 kyu
# Array.diff
# Python:
def array_diff(a, b):
    return [item for item in a if item not in b]


# 8 kyu
# Beginner Series #1 School Paperwork
# Python:
def paperwork(n, m):
    return n * m if n>-1 and m>-1 else 0

# 6 kyu
# Sort the odd
# Python:
def sort_array(source_array):
    x = sorted(list(filter(lambda x: x % 2!= 0, source_array)))
    k = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = x[k]
            k += 1
    return source_array