# 오르막수_BOJ11057

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 자리수를 input 받고
dp = [1] * 10               # 경우의 수를 저장할 리스트를 생성한다
for i in range(1, N):       # 자리수를 반복하고
    tmp = [1] * 10          # 앞자리 숫자에 따라 다음에 나올 경우의 수를 저장할 리스트를 생성한다
    A = sum(dp)             # 이전 자리수의 오르막 수 의 개수를 A에 저장하고
    for d in range(10):     # 각 자리수를 반복해서
        tmp[d] *= A         # 이전 오르막수가 d로 끝나는 경우의 수를 tmp[d]에 저장하고
        A -= dp[d]          # A에서 dp[d]를 빼서 그 다음 오르막 수의 경우의 수를 계산하기 위한 A를 저장한다
    dp = tmp[::]            # 모든 자리수의 탐색을 마쳤다면 dp를 tmp로 갱신한다
print(sum(dp) % 10007)      # 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다