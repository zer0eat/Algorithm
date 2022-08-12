# Brute force

# 방법_1
t = 'this is book'
p = 'is'
print(p in t)

# 방법_2
def func1(t, p):
    for i in range(len(t) - len(p) + 1):
        for j in range(len(p)):
            if t[i + j] != p[j]:
                break
        else:
            return i
    return -1
print(func1(t, p))

# 방법_3
def func2(t, p):
    m = len(p)
    for a in range(len(t) - len(p) + 1):
        if t[a:a+m] == p:
            return a
    return -1
print(func2(t, p))

# 방법_4
def func3(t, p):
    i = 0
    j = 0
    while j<len(p) and i<len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return i - len(p)
    else:
        return -1
print(func3(t, p))