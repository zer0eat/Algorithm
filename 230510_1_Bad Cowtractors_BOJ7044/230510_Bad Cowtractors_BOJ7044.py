# Bad Cowtractors_BOJ7044

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                # N 헛간의 수 / M 헛간을 연결하는 길
road = [[] for _ in range(N+1)]                 # 길의 정보를 저장할 리스트 생성
for _ in range(M):                              # 길의 수를 반복해서
    a, b, c = map(int, input().split())         # a, b 헛간의 정보와 c 비용을 input 받고 
    road[a-1].append([-c, b-1])                 # a 헛간에서 이동할 수 있는 곳을 [비용, 연결 헛간]을 append
    road[b-1].append([-c, a-1])                 # b 헛간에서 이동할 수 있는 곳을 [비용, 연결 헛간]을 append

ans = 0                                         # 정답을 저장할 변수를 생성하고
visited = [0] * N                               # 방문 기록을 저장할 리스트를 생성한다
tmp = [[0, 0]]                                  # 시작점을 넣은 tmp 리스트를 생성하고
while tmp:                                      # tmp가 빌 때까지 반복해서
    cost, node = heapq.heappop(tmp)             # tmp에서 heappop해서 비용과 연결 헛간 정보를 저장한다
    if visited[node] == 0:                      # 연결 헛간이 방문 전이라면
        ans += cost                             # ans에 비용을 더하고
        visited[node] = 1                       # 연결 헛간을 방문표시를 한다
        for r in road[node]:                    # 연결 헛간에서 갈 수 있는 길을 반복해서
            if visited[r[1]] == 0:              # 도착지가 방문 전이라면
                heapq.heappush(tmp, r)          # tmp에 heappush한다

if sum(visited) == N:                           # 모든 헛간을 방문 가능하다면
    print(-ans)                                 # 최대 비용을 출력하고
else:                                           # 모든 헛간을 방문할 수 없다면
    print(-1)                                   # -1 을 출력한다