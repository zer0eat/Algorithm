# 제곱수의합_BOJ1699

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N = int(input())                                # 자연수 N을 input 받고
dp = [100001] * (N+1)                           # N번 인덱스까지 리스트를 생성한다
dp[0] = 0                                       # 0을 만들 수 있는 경우의 수는 없으므로 0으로 저장한다
for k in range(1, N+1):                         # 1부터 N까지 반복해서
    Q = int(math.sqrt(k))                       # k의 제곱근에서 소수점을 버린 정수를 Q에 저장한다
    for i in range(Q, 0, -1):                   # Q부터 1까지 역순으로 반복해서
        tmp = 0                                 # 제곱수의 개수를 저장할 변수를 생성하고
        tmpk = k                                # k를 tmpk에 저장한다
        tmp += tmpk // (i*i)                    # i의 제곱수로 나눈 몫을 tmp에 저장하고
        if tmp > dp[k]:                         # tmp가 dp[k]보다 크다면
            break                               # for문을 break한다
        tmpk = tmpk % (i*i)                     # tmpk를 i의 제곱수로 나눈 나머지로 저장하고
        dp[k] = min(dp[k], dp[tmpk] + tmp)      # 저장된 dp[k]와 dp[tmpk]와 tmp의 합 중 작은 값을 dp[k]에 저장한다
print(dp[N])                                    # 주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다