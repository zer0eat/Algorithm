# Traveling SCCC President_BOJ28119

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, S = map(int, input().split())                         # N 건물의 수 / M 도로의 수 / 시작 건물
road = [[] for _ in range(N)]                               # 도로의 정보를 저장할 리스트 생성
for _ in range(M):                                          # 도로의 수를 반복해서
    a, b, c = map(int, input().split())                     # a,b 건물의 정보와 c 도로의 비용을 input 받고
    road[a-1].append([c, b-1])                              # a에 [비용, 도착 건물]를 append
    road[b-1].append([c, a-1])                              # b에 [비용, 도착 건물]를 append

ans = 0                                                     # 최소 비용을 저장할 변수 생성
cnt = 0                                                     # 방문 건물의 수를 저장할 변수 생성
visited = [0] * N                                           # 방문 표시를 할 리스트 생성
tmp = [[0, S-1]]                                            # 시작점을 넣고 리스트 생성
while cnt < N:                                              # 방문지가 N개가 될때까지 반복해서
    cost, node = heapq.heappop(tmp)                         # 비용과 건물를 heappop한 후
    if visited[node] == 0:                                  # 해당 건물이 방문 전이라면
        visited[node] = 1                                   # 방문 표시를 하고
        ans += cost                                         # ans에 비용을 더하고
        cnt += 1                                            # 방문지의 수를 1 더한다
        for r in road[node]:                                # 건물과 연결된 도로를 반복해서
            if visited[r[1]] == 0:                          # 도로의 도착지가 방문 전이라면
                heapq.heappush(tmp, r)                      # tmp에 heappush 한다
print(ans)                                                  # 최소 비용을 출력한다