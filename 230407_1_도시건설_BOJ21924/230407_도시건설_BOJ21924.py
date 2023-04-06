# 도시건설_BOJ21924

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 건물의 수 / M 도로의 개수

road = [[] for _ in range(N)]               # 도로의 연결을 저장할 리스트 생성
total = 0                                   # 전체 비용을 저장할 변수 생성
for _ in range(M):                          # 도로의 수를 반복해서
    a, b, c = map(int, input().split())     # a 건물 b 건물 c ab 건물사이 도로의 비용을 input 받는다
    total += c                              # total에 도로 비용을 더하고
    road[a-1].append([c, b-1])              # a-1 인덱스에 [비용, 연결할 건물 인덱스]를 append
    road[b-1].append([c, a-1])              # b-1 인덱스에 [비용, 연결할 건물 인덱스]를 append

visited = [0] * N                           # 방문표시를 할 리스트를 생성하고
ans = 0                                     # 최소 비용을 저장할 변수 생성
tmp = [[0, 0]]                              # tmp 리스트에 [비용 0, 출발 건물]을 넣어 생성하고
while tmp:                                  # tmp가 빌때까지 반복해서
    cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 연결할 건물을 node에 건설할 비용을 cost에 저장
    if visited[node] == 0:                  # node 건물이 방문 전이라면
        visited[node] = 1                   # node 건물을 방문표시하고
        ans += cost                         # ans에 비용을 더한다
        for r in road[node]:                # 연결할 건물에서 갈 수 있는 건물을 반복해서
            if visited[r[1]] == 0:          # 갈 수 있는 건물이 방문전이라면
                heapq.heappush(tmp, r)      # tmp에 r을 heappush 한다

if sum(visited) == N:                       # visited의 합이 N이라 모든 건물이 연결되었다면
    print(total - ans)                      # 모든 비용에서 최소비용을 빼서 절약된 금액을 출력하고
else:                                       # N이 아니라면 모든 건물을 연결할 수 없으므로
    print(-1)                               # -1을 출력한다