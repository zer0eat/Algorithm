# 종이붙이기_13806_while 사용

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())            # 테스트 케이스
for t in range(T):
    N = int(input())        # 가로의 길이
    N = N // 10
    lst = [1]               # N이 1일 때 값을 lst에 입력하고 시작
    n = 2                   # N이 2일 때 부터 값을 찾기위해 인덱스 n을 2로 설정
    while n <= N:           # N 이하의 값을 구하기 위해 반복
        x = 2 ** n - lst[(n - 1)-1]     # 2**N = f(N) + f(N-1) 이므로  f(N) = 2**N - f(N-1) 인덱스는 0부터 시작해서 -1을 추가로 해줌
        lst.append(x)       # 구한 값을 리스트에 추가하고
        n += 1              # 다음 인덱스로 넘어감
    print(f'#{t + 1}', lst[N-1])        # 리스트의 마지막 값이 N일 때 붙일 수 있는 종이의 수







