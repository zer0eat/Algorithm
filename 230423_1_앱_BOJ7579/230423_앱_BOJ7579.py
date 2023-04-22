# 앱_BOJ7579

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                        # N 앱의 개수 / M 삭제해야하는 메모리
memory = list(map(int, input().split()))                # 앱마다 메모리를 리스트로 받고
cost = list(map(int, input().split()))                  # 앱마다 삭제 비용을 리스트로 받는다
ans = sum(cost)                                         # 모든 앱을 끌 때 비용을 ans에 저장한다

visited = [[0]*(sum(cost)+1) for _ in range(N+1)]       # 비용마다 줄일 수 있는 메모리를 저장할 리스트 생성

for n in range(1, N+1):                                 # 앱의 수만큼 반복해서
    for m in range(sum(cost)+1):                        # 모든 앱이 삭제 될 때 비용만큼 반복한다
        if m >= cost[n-1]:                              # 현재 삭제할 수 있는 비용이 n번 째 앱을 끌 수 있을만큼 크다면
            visited[n][m] = max(visited[n-1][m], visited[n-1][m-cost[n-1]]+memory[n-1]) # 현재 앱을 끄지 않고 m비용 끌 수 있는 메모리와 현재앱을 끄고 남은 비용으로 끌 수 있는 메모리 중 큰 값으로 저장
        else:                                           # 현재 삭제할 수 있는 비용이 n번 째 앱을 끌 수 없다면
            visited[n][m] = visited[n - 1][m]           # visited[n][m]에 현재 앱을 끄지 않고 m비용 끌 수 있는 메모리를 저장
        if visited[n][m] >= M:                          # 현재 삭제된 메모리가 삭제해야할 메모리보다 크다면
            ans = min(ans, m)                           # ans에 저장된 비용과 현재비용 중 작은 값을 ans에 저장한다
print(ans)                                              # 모든 반복을 마치고 M 메모리를 삭제할 때 최소비용을 출력한다