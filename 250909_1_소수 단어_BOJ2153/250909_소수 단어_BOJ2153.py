# 소수 단어_BOJ2153

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()             # 문자를 input받고
ans = 0                         # 숫자를 저장할 변수를 생성하고
for n in N:                     # 문자를 반복해서
    if n.islower():             # 문자가 소문자라면
        ans += ord(n)-96        # 1부터 26까지 대응되는 숫자를 더하고
    else:                       # 문자가 대문자라면
        ans += ord(n)-38        # 27부터 52까지 대응되는 숫자를 더하고
for i in range(2, ans):         # 숫자를 반복해서
    if ans % i == 0:            # 숫자가 나눠 떨어진다면
        print('It is not a prime word.')    # 소수가 아니라고 출력하고
        quit()                  # 숫자가 나눠 떨어지지 않는다면
print('It is a prime word.')    # 소수라고 출력한다