# 지름길_BOJ1446

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input.txt 열기
N, D = map(int, input().split())                            # N 지름길의 개수 / D 고속도로의 길이를 input 받고
dp = [i for i in range(D+1)]                                # 길이별 최소 거리를 저장할 dp 리스트를 생성하고
lst = [list(map(int, input().split())) for _ in range(N)]   # 지름길을 input 받아 리스트에 저장한다
lst.sort()                                                  # 지름길의 시작점을 기준으로 오름차순 정렬하고
for i in range(N):                                          # 지름길의 수를 반복해서
    s, e, cost = lst[i]                                     # i번째 지름길의 시작 / 끝 / 거리를 변수에 저장하고
    if e < D+1:                                             # 지름길의 끝이 도착점보다 작다면
        dp[e] = min(dp[e], dp[s]+cost)                      # 지름길의 끝에 저장된 거리와 시작점에서 지름길을 통해 오는 거리 중 더 작은 거리를 지름길의 끝에 저장하고
        for j in range(e+1, D+1):                           # 지름길의 끝 지점 다음부터 끝까지 반복해서
            dp[j] = min(dp[j], dp[j-1]+1)                   # 해당지점과 이전지점에서 1이동한 거리중 더 작은 값을 저장한다
print(dp[-1])                                               # 도착지까지 이동하는 거리중 최소거리를 출력한다