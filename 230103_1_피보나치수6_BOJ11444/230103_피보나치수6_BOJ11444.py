# 피보나치수6_BOJ11444

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def find(N):
    if not fibo.get(N):                                                 # fibo 딕셔너리에 key가 N인 요소가 없다면
        if N % 2:                                                       # N이 홀수일 때
            n = (N+1) // 2                                              # n에 N+1을 2로 나눈 숫자를 저장하고
            fibo[N] = (find(n)**2 + find(n-1)**2) % 1000000007          # key가 N인 value를 (find(n)**2 + find(n-1)**2) % 1000000007로 저장한다
        else:                                                           # N이 짝수일 때
            n = N // 2                                                  # n에 N을 2로 나눈 숫자를 저장하고
            fibo[N] = (find(n)**2 + 2*find(n-1)*find(n)) % 1000000007   # key가 N인 value를 (find(n)**2 + 2*find(n-1)*find(n)) % 1000000007로 저장한다
    return fibo[N]                                                      # N번째 피보나치수를 리턴한다

# input 받기
N = int(sys.stdin.readline().strip())                                   # 찾고자하는 피보나치 수의 순서를 input
fibo = dict()                                                           # 딕셔너리를 생성하고
fibo[0] = 0                                                             # key가 0 / value가 0인 요소 생성
fibo[1] = 1                                                             # key가 1 / value가 1인 요소 생성
fibo[2] = 1                                                             # key가 2 / value가 1인 요소 생성

print(find(N))                                                          # find 함수로 찾은 N번째 피보나치 수를 출력한다
