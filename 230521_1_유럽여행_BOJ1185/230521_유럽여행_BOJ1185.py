# 유럽여행_BOJ1185

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                            # N 나라의 수 / M 길의 수
money = []                                                  # 나라 방문 비용을 저장할 리스트 생성
for _ in range(N):                                          # 나라의 수만큼 반복해서
    money.append(int(input()))                              # money 리스트에 방문 비용을 append
road = [[] for _ in range(N)]                               # 길의 정보를 저장할 리스트 생성
for _ in range(M):                                          # 길의 수를 반복해서
    a, b, c = map(int, input().split())                     # a, b 나라 정보와 c 비용을 input 받고
    road[a-1].append([2*c+money[a-1]+money[b-1], b-1])      # a에 [a,b 왕복 비용, b]를 append
    road[b-1].append([2*c+money[a-1]+money[b-1], a-1])      # b에 [a,b 왕복 비용, a]를 append

ans = 0                                                     # 최소 비용을 저장할 변수생성
cnt = 0                                                     # 방문 나라의 수를 저장할 변수 생성
visited = [0] * N                                           # 방문 표시를 할 리스트 생성
tmp = [[0, 0]]                                              # tmp에 시작점을 넣고 리스트 생성
while cnt < N:                                              # cnt가 N이 되어 모든 나라를 방문할 때까지 반복해서
    cost, node = heapq.heappop(tmp)                         # 방문 비용과 방문나라를 heappop해서
    if visited[node] == 0:                                  # 방문나라가 방문 전이라면
        visited[node] = 1                                   # 방문표시를 하고
        ans += cost                                         # 비용을 더한 후
        cnt += 1                                            # cnt에 1을 추가한다
        for r in road[node]:                                # 방문 나라에서 연결된 길을 반복해서
            if visited[r[1]] == 0:                          # 연결된 길의 도착지가 방문 전이라면
                heapq.heappush(tmp, r)                      # tmp에 길의 도착지의 비용과 나라를 heappush
print(ans + min(money))                                     # 최소 비용으로 모든 나라를 방문하는 비용과 마지막으로 출발지로 돌아오는 최소 비용을 출력