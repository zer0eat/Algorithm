# 구멍_BOJ 33571

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()     # 문자를 input받고
ans = 0                 # 정답을 저장할 변수를 생성하고
one = ['A','a','b','D','d','e','g','O','o','P','p','Q','q','R','@'] # 구멍이 한개인 리스트를 만들고
two = 'B'               # 구멍이 두개인 변수를 만든다
for s in S:             # 문자를 반복해서
    if s in one:        # 구멍이 한개라면
        ans += 1        # 정답에 1을 추가하고
    elif s == two:      # 구멍이 두개라면
        ans += 2        # 정답에 2를 추가하고
print(ans)              # 정답을 출력한다