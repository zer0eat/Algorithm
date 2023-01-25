# RGB거리2_BOJ17404

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline().strip())                                               # 집의 개수
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]            # N개의 줄에 각 집을 빨강, 초록, 파랑으로 색칠하는데 드는 비용 input받음
ans = []                                                                            # 첫번째 집의 색을 골라 놓고 첫번째와 마지막 집의 색이 다를 때 최소비용을 저장할 리스트 생성

for q in range(3):                                                                  # RGB 세번 반복해서
    dp = [[0]*3 for _ in range(N)]                                                  # 집의 개수만큼 빈 행렬을 만든다
    for j in range(3):                                                              # RGB 세번 반복해서
        if q == j:                                                                  # q의 색으로 칠하기로 했을 때 j와 같다면
            dp[0][j] = house[0][j]                                                  # dp[0][j]에 진짜 드는 비용으로 저장하고
        else:                                                                       # j와 다르다면
            dp[0][j] = 1000000                                                      # dp[0][j]에 1000000 최대 비용으로 저장한다
    for i in range(1, N):                                                           # 1부터 N-1까지 반복해서(q색상만 정상비용이므로 q색상으로 시작)
        dp[i][0] = min(house[i][0] + dp[i - 1][1], house[i][0] + dp[i - 1][2])      # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 빨강으로 칠하는데 드는 가장 최소 비용으로 바꿔 dp에 저장
        dp[i][1] = min(house[i][1] + dp[i - 1][0], house[i][1] + dp[i - 1][2])      # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 초록으로 칠하는데 드는 가장 최소 비용으로 바꿔 dp에 저장
        dp[i][2] = min(house[i][2] + dp[i - 1][0], house[i][2] + dp[i - 1][1])      # 인덱스가 i번인 집을 앞집(i-1)과 겹치지 않게 파랑으로 칠하는데 드는 가장 최소 비용으로 바꿔 dp에 저장
    else:                                                                           # 반복을 마쳤으면
        dp[N - 1].pop(q)                                                            # 마지막 집에서 첫번째 집과 겹치는 경우를 pop해서 빼주고
        ans.append(min(dp[N-1]))                                                    # 나머지 중 저렴한 값을 ans에 append
else:                                                                               # RGB 모두 반복해서
    print(min(ans))                                                                 # 셋 중 최소비용을 출력한다