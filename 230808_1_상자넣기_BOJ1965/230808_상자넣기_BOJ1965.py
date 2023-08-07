# 상자넣기_BOJ1965

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 상자의 개수를 input 받고
lst = list(map(int, input().split()))       # 상자의 크기를 리스트로 input 받는다
dp = [1] * N                                # 순서 별 상자를 가장 많이 넣는 경우를 저장할 리스트를 생성하고
for i in range(1, N):                       # 2번째 상자부터 N번째 상자까지 반복하고
    for j in range(i):                      # i번 이전의 상자를 반복한다
        if lst[i] > lst[j]:                 # i번과 i번 이전의 상자를 비교했을 때 i가 더 큰 경우
            dp[i] = max(dp[i], dp[j]+1)     # 현재 저장된 최대 상자 개수와 j번 상자를 담았을 때 상자 개수 중 더 큰 값으로 갱신한다
print(max(dp))                              # 모든 상자를 비교한 후 한 줄에 넣을 수 있는 최대의 상자 개수를 출력한다
