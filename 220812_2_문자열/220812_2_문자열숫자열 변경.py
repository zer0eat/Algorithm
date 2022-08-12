# 문자열을 숫자로 변경하기
# int()와 같은 atoi()함수 만들기
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

s = '123'
a = atoi(s)
print(a)
print(a+10)

# 숫자열을 문자로 변경하기
# str()와 같은 itoa()함수 만들기
def itoa(num):
    ans = ''
    while num:
        num, reminder = divmod(num, 10)
        # num, reminder = num//10, num%10
        ans = chr(reminder + ord('0')) + ans
    return ans


u = 123
b = itoa(u)
print(type(b), b)
