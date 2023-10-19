# 내려가기_BOJ2094

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 내려갈 줄의 수를 input 받고
jido = list(map(int, input().split()))                      # 내려가는 지도의 첫 줄을 input 받는다
max_dp = jido[:]                                            # 최대 값을 저장할 dp를 지도의 첫줄을 넣어 만들고
min_dp = jido[:]                                            # 최소 값을 저장할 dp를 지도의 첫줄을 넣어 만든다
max_tmp = [0] * 3                                           # 다음 행의 최대값을 구하기 위한 리스트를 생성하고
min_tmp = [0] * 3                                           # 다음 행으 최소값을 구하기 위한 리스트를 생성한다
for i in range(1, N):                                       # 1번부터 N-1 행까지 반복하고
    jido = list(map(int, input().split()))                  # i행의 지도를 input 받고
    for j in range(3):                                      # 각 열을 반복해서
        if j == 0:                                                                              # 0번째 열이면
            max_tmp[j] = max(jido[j] + max_dp[j], jido[j] + max_dp[j+1])                        # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j+1번째 열 값 중 큰 값을 더해 max_tmp[j]에 저장한다
            min_tmp[j] = min(jido[j] + min_dp[j], jido[j] + min_dp[j+1])                        # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j+1번째 열 값 중 작은 값을 더해 min_tmp[j]에 저장한다
        elif j == 2:                                                                            # 마지막 열이면
            max_tmp[j] = max(jido[j] + max_dp[j-1], jido[j] + max_dp[j])                        # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j-1번째 열 값 중 큰 값을 더해 max_tmp[j]에 저장한다
            min_tmp[j] = min(jido[j] + min_dp[j-1], jido[j] + min_dp[j])                        # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j-1번째 열 값 중 작은 값을 더해 min_tmp[j]에 저장한다
        else:                                                                                   # 나머지 열이면
            max_tmp[j] = max(jido[j] + max_dp[j-1], jido[j] + max_dp[j], jido[j] + max_dp[j+1]) # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j-1번째 열 / j+1번째 열 값 중 큰 값을 더해 max_tmp[j]에 저장한다
            min_tmp[j] = min(jido[j] + min_dp[j-1], jido[j] + min_dp[j], jido[j] + min_dp[j+1]) # i번째 행 j번째 열의 값과 i-1번째 행 j번째 열 / j-1번째 열 / j+1번째 열 값 중 작은 값을 더해 min_tmp[j]에 저장한다
    else:                                                   # 모든 열의 탐색을 마쳤다면
        max_dp = max_tmp[:]                                 # max_dp에 다음 행의 각 열마다 최대 값을 저장하고
        min_dp = min_tmp[:]                                 # min_dp에 다음 행의 각 열마다 최소 값을 저장한다
ans_max = max(max_dp)                                       # 얻을 수 있는 최대 점수를 ans_max에 저장하고
ans_min = min(min_dp)                                       # 얻을 수 있는 최소 점수를 ans_min에 저장해서
print(ans_max, ans_min)                                     # 최대 점수와 최소 점수를 띄어서 출력한다