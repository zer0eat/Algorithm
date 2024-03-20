# 자두나무_BOJ2240

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T, W = map(int, input().split())                # T 시간 / W 이동횟수를 input 받고
jadu = [0] + [int(input()) for _ in range(T)]   # 시간별 자두가 떨어지는 나무를 리스트로 input 받고
dp = [[0] * (W+1) for _ in range(T+1)]          # 최대 자두를 저장할 dp를 생성한다
if jadu[1] == 1:                                # 1번째 자두가 떨어지는 나무가 1번 나무라면
    dp[1][0] = 1                                # 1행 0열에 1을 추가하고
else:                                           # 1번째 자두가 떨어지는 나무가 2번 나무라면
    dp[1][1] = 1                                # 1행 1열에 1을 추가한다
for i in range(2, T+1):                         # 2번째 부터 끝까지 반복해서
    for j in range(W+1):                        # 이동횟수를 반복한 후
        if j % 2 == 0:                          # 1번 나무 밑에 있다면
            a = jadu[i] % 2                     # 1번 나무에 떨어진 경우 a에 1을 저장하고
        else:                                   # 2번 나무 밑에 있다면
            a = jadu[i] // 2                    # 2번 나무에 떨어진 경우 a에 1을 저장한다
        dp[i][j] = max(dp[i-1][0:j+1]) + a      # i번째 자두를 j번의 이동에 받을 때 받을 수 있는 자두의 최대 개수를 저장한다
print(max(dp[-1]))                              # 자두가 받을 수 있는 자두의 최대 개수를 출력한다