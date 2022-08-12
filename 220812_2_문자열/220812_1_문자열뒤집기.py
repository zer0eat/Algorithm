# 문자열 뒤집기

# 방법 1 _ 파이썬만 가능
s = 'Reverse this strings'
print(s[::-1])

# 방법 2 _ 다른 언어에서도 가능
a = list(s)
a.reverse()
a = ''.join(a)
print(a)

# 방법 3 _ for문 이용
ans = ''
for char in s:
    ans = char + ans
print(ans)

# 방법 4 _ for문 이용
ans2 = ''
for idx in range(len(s)-1,-1,-1):
    ans2 += s[idx]
print(ans2)

