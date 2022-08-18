# 종이붙이기_13806_for 사용

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())            # 테스트 케이스
for t in range(T):
    N = int(input())        # 가로의 길이
    N = N // 10
    lst = [1]               # N이 1일 때 값을 lst에 입력하고 시작

    for n in range(N):      # N 이하의 값을 구하기 위해 반복
        if n == 0:          # n이 0이면 패스
            pass
        elif n > 0:         # 0이 아닐 때
            x = 2**(n+1) - lst[n-1] # 2**N = f(N) + f(N-1) 이므로  f(N) = 2**N - f(N-1) 인덱스는 0부터 시작해서 2**N의 N의 값에 +1을 추가로 해줌
            lst.append(x)   # 리스트에 추가

    print(f'#{t+1}', lst[N-1])  # 리스트의 마지막 값이 붙일 수 있는 조각의 수






