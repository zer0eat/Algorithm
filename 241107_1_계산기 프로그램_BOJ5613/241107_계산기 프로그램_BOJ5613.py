# 계산기 프로그램_BOJ5613

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = int(input())      # 시작 숫자를 input 받고
while 1:                # break가 나올 때까지 반복해서
    A = input().strip() # 연산자를 input 받고
    if A == '=':        # 등호라면
        print(ans)      # 답을 출력하고
        break           # 종료한다
    N = int(input())    # 숫자를 입력받고
    if A == '+':        # 연산자가 + 라면
        ans += N        # 정답에 N을 더한다
    elif A == '-':      # 연산자가 - 라면
        ans -= N        # 정답에 N을 뺀다
    elif A == '*':      # 연산자가 * 이라면
        ans *= N        # 정답에 N을 곱한다
    else:               # 연산자가 / 라면
        ans //= N       # 정답에 N을 나누고 나머지는 버린다