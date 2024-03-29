# 개업_BOJ13910

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                        # N 짜장면의 수 / M 웍의 개수를 input 받고
S = list(map(int, input().split()))                     # 웍의 크기를 리스트로 input 받는다
wok = set(S)                                            # wok으로 만들 수 있는 짜장면의 수를 저장할 set을 생성하고
for i in range(M):                                      # 웍의 개수를 반복하고
    for j in range(i+1, M):                             # 그다음 웍을 반복해서
        wok.add(S[i]+S[j])                              # 두 웍으로 만들 수 있는 짜장면의 수를 wok에 add한다
dp = [-1] * (N+1)                                       # 정답을 저장할 dp를 생성하고
dp[0] = 0                                               # 0그릇일 때 만들 수 있는 요리횟수를 저장한다
for w in wok:                                           # 만들 수 있는 짜장면의 수를 반복해서
    for n in range(N-w+1):                              # w인분 만들었을 때 N인분이 되는 수를 반복해서
        if dp[n] != -1:                                 # n인 분을 만든적이 있을 때
            if dp[w+n] == -1 or dp[n+w] > dp[n] + 1:    # w+n인분을 만든 적이 없거나 n+w인분을 만들 때 n인분에서 한번 더 조리한 수가 더 적다면
                dp[w+n] = dp[n]+1                       # w+n인분을 만들기 위해 dp[n] + 1번 요리를 해야한다고 저장한다
print(dp[N])                                            # N인분을 만들기 위한 요리횟수를 출력한다