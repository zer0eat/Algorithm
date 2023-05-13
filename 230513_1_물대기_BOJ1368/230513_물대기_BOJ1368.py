# 물대기_BOJ1368

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                                # 논의 수
tmp = []                                                        # 물을 대기 위해 필요한 정보를 저장할 리스트 생성
well = []                                                       # 우물을 파는 비용을 저장하기 위한 리스트 생성
for i in range(N):                                              # 논의 수를 반복해서
    A = int(input())                                            # 우물을 파는 비용을 input 받고
    heapq.heappush(tmp, [A, i])                                 # tmp에 [비용, 논의 번호]를 heappush
    well.append(A)                                              # well에 우물 비용을 append
road = [list(map(int, input().split())) for _ in range(N)]      # 논과 논 사이에 길을 팔 때 드는 비용을 행렬에 input

ans = 0                                                         # 최소비용을 저장할 변수 생성
visited = [0] * N                                               # 방문 표시를 할 리스트 생성
while tmp:                                                      # tmp가 빌 때까지 반복해서
    cost, node = heapq.heappop(tmp)                             # 비용과 논 정보를 heappop하고
    if visited[node] == 0:                                      # 논이 방문 전이라면
        visited[node] = 1                                       # 방문표시를 하고
        ans += cost                                             # 비용을 ans에 append
        for x in range(N):                                      # 논을 반복해서
            if x != node:                                       # node의 논과 다른 논인 경우에만
                if well[x] > road[node][x]:                     # 만약 우물을 파는 비용이 논을 연결하는 비용보다 크다면
                    well[x] = road[node][x]                     # 우물을 파는 비용을 논을 연결하는 비용으로 바꾼 후
                    heapq.heappush(tmp, [well[x], x])           # tmp에 [비용, 논의 번호]를 heappush
print(ans)                                                      # while문을 마친 후 최소 비용을 출력한다