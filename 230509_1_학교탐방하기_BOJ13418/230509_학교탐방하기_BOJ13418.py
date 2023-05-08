# 학교탐방하기_BOJ13418

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 건물의 수 / M 길의 수
road = [[] for _ in range(N+1)]             # 피도로가 가장 많이 생기는 길을 찾기 위한 리스트 생성
road2 = [[] for _ in range(N+1)]            # 피도로가 가장 적게 생기는 길을 찾기 위한 리스트 생성
for _ in range(M+1):                        # 길의 수를 반복해서
    a, b, c = map(int, input().split())     # a, b 건물과 c 피로도를 input 받는다
    road[a].append([c, b])                  # a 건물에서 이동할 수 있는 곳을 [피로도, 연결 건물]을 append
    road[b].append([c, a])                  # b 건물에서 이동할 수 있는 곳을 [피로도, 연결 건물]을 append
    road2[a].append([-c, b])                # a 건물에서 이동할 수 있는 곳을 [-피로도, 연결 건물]을 append
    road2[b].append([-c, a])                # b 건물에서 이동할 수 있는 곳을 [-피로도, 연결 건물]을 append

ans = 0                                     # 최대 피로도를 저장할 변수생성
tmp = [road[0][0]]                          # tmp에 입구에서 1번 건물로 이동하는 원소를 넣고 리스트 생성
visited = [0] * (N+1)                       # 방문 기록을 저장할 리스트 생성
visited[0] = 1                              # 입구를 방문표시한 후
cnt = 0                                     # 방문한 건물의 수를 저장할 변수를 생성한다
while cnt < N+1:                            # cnt가 N이 될 때까지 반복해서
    cost, node = heapq.heappop(tmp)         # 피로도, 연결 건물을 tmp에서 heappop해서 저장한 후
    if visited[node] == 0:                  # 연결 건물이 방문 전이라면
        visited[node] = 1                   # 연결 건물을 방문 표시하고
        cnt += 1                            # 방문 건물의 수를 1 추가한다
        ans += cost                         # ans에 피로도를 더한다
        for r in road[node]:                # node와 연결된 길을 반복해서
            if visited[r[1]] == 0:          # 연결된 길의 도착지가 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 길을 heappush한다

ans2 = 0                                    # 최소 피로도를 저장할 변수생성
tmp2 = [road2[0][0]]                        # tmp2에 입구에서 1번 건물로 이동하는 원소를 넣고 리스트 생성
visited2 = [0] * (N+1)                      # 방문 기록을 저장할 리스트 생성
visited2[0] = 1                             # 입구를 방문표시한 후
cnt2 = 0                                    # 방문한 건물의 수를 저장할 변수를 생성한다
while cnt2 < N:                             # cnt2가 N이 될 때까지 반복해서
    cost, node = heapq.heappop(tmp2)        # 피로도, 연결 건물을 tmp2에서 heappop해서 저장한 후
    if visited2[node] == 0:                 # 연결 건물이 방문 전이라면
        visited2[node] = 1                  # 연결 건물을 방문 표시하고
        cnt2 += 1                           # 방문 건물의 수를 1 추가한다
        ans2 += cost                        # ans2에 피로도를 더한다
        for r in road2[node]:               # node와 연결된 길을 반복해서
            if visited2[r[1]] == 0:         # 연결된 길의 도착지가 방문 전이라면
                heapq.heappush(tmp2, r)     # tmp에 길을 heappush한다

print((N-ans)**2 - (N+ans2)**2)             # 최대 피로도와 최소 피로도의 차를 출력한다