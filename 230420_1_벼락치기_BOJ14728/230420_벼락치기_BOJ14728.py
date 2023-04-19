# 벼락치기_BOJ14728

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, T = map(int, input().split())                # N 단원개수 / T 공부할 총 시간
visited = [[0]*(T+1) for _ in range(N)]         # 시간별로 공부하여 얻을 수 있는 최대치를 저장할 리스트 생성

K, S = map(int, input().split())                # K 단원 별 공부 시간 / S 단원 별 배점
for k in range(K, T+1):                         # K 시간부터 T까지 반복해서
    visited[0][k] = S                           # K 시간 이후부터 S 점수를 받을 수 있기 때문에 원소를 S로 저장한다

for n in range(1, N):                           # 인덱스 1부터 단원개수를 반복해서
    K, S = map(int, input().split())            # K 단원 별 공부 시간 / S 단원 별 배점을 input 받고
    for i in range(T+1):                        # 공부할 수 있는 시간을 반복해서
        if i < K:                               # 공부할 수 있는 시간이 단원 별 공부시간 보다 짧다면
            visited[n][i] = visited[n-1][i]     # 해당과목은 공부할 수 없으므로 이전 행의 단원별 배점을 저장한다
        else:                                   # 공부할 수 있는 시간이 단웝 별 공부시간 보다 길다면
            visited[n][i] = max(visited[n-1][i-K] + S, visited[n-1][i]) # 이전 행의 배점 / 현재 과목 배점 남은시간 동안 공부해서 받을 수 있는 배점 중 큰 점수로 저장한다
print(visited[N-1][T])                          # 모든 반복이 끝났다면 T시간동안 얻을 수 있는 최대 배점을 출력한다