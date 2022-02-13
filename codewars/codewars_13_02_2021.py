# 6 kyu
# Replace With Alphabet Position
# Python:
def alphabet_position(text):
    text = text.lower()
    arr = ""
    for i in text:
        if i.isalpha():
            arr += str(ord(i) - 96) + " "
    return arr[:-1]

# 6 kyu
# Split Strings
# Python:
def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    arr = [s[i:i+2] for i in range(0, len(s), 2)]
    return arr

# 7 kyu
# Get the Middle Character
# Python:
def get_middle(s):
    l = len(s)
    m = l // 2
    if l % 2 == 0:
        return s[m-1:m+1]
    else:
        return s[m]
    

# 7 kyu
# Regex validate PIN code
# Python:
import re
def validate_pin(pin):
    l = len(pin)
    if l == 4 or l == 6:
        if pin.isdigit():
            return True
    return False

# 7 kyu
# Beginner Series #3 Sum of Numbers
# Python:
def get_sum(a,b):
    if a > b:
        a,b = b,a
    s = (a + b) * (b - a + 1) // 2
    return s

# 8 kyu
# Remove String Spaces
# Python:
def no_space(x):
    return "".join(x.split())

# 7 kyu
# Is this a triangle?
# Python:
def is_triangle(a, b, c):
    if a+b <= c or b+c <= a or a+c <= b:
        return False
    else:
        return True

# 7 kyu
# Categorize New Member
# Python:
def open_or_senior(data):
    output = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

# 8 kyu
# Reversed Strings
# Python:
def solution(string):
    return string[ : : -1]

# 8 kyu
# Multiply
# Python:
def multiply(a, b):
    return a * b

# 8 kyu
# Counting sheep...
def count_sheeps(sheep):
    c = 0
    for i in sheep:
        if i:
            c += 1
    return c

