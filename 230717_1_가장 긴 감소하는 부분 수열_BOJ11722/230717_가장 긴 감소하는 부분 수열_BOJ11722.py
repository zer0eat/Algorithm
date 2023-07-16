# 가장 긴 감소하는 부분 수열_BOJ11722

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 수열의 크기
lst = list(map(int, input().split()))       # 수열을 리스트로 input 받는다
dp = [1] * N                                # 수열의 인덱스마다 최대 수열이 되는 값을 저장할 리스트 생성
for i in range(1, N):                       # 1부터 N-1까지 반복해서
    for j in range(i):                      # i번째 원소 이전의 원소를 반복해서
        if lst[i] < lst[j]:                 # i번째 원소가 j보다 작을 때
            dp[i] = max(dp[i], dp[j]+1)     # i의 최대 수열의 길이를 현재 저장된 i번째 정답과 j보다 1 증가한 값 중 큰 값으로 저장한다
print(max(dp))                              # dp에 저장된 최대 수열의 길이 중 가장 큰 값을 출력한다