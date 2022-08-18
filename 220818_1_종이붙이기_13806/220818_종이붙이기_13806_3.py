# 종이붙이기_13806_def 사용

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 함수 만들기
def f(n):                       # 가로의 길이에 따른 붙일 종이 수 구하는 함수
    if n == 1:                  # 가로의 길이가 10일 때 1을 리턴한다
        return 1
    else:                       # 가로의 길이가 10 이상일 때
        return 2**n - f(n-1)    # 2**N = f(N) + f(N-1) 이므로  f(N) = 2**N - f(N-1)

# input 받기
T = int(input())            # 테스트케이스
for t in range(T):
    N = int(input())        # 가로의 길이
    N = N // 10

    print(f'#{t + 1}', f(N))







