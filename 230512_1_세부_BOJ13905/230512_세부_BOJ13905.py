# 세부_BOJ13905

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                # N 섬에 존재하는 집의 수 / M 다리의 수
road = [[] for _ in range(N)]                   # 다리의 정보를 저장할 리스트 생성
start, end = map(int, input().split())          # 출발섬, 도착점의 정보를 input 받고
for _ in range(M):                              # 다리의 수를 반복해서
    a, b, c = map(int, input().split())         # 연결된 두섬 a,b와 지나갈 수 있는 무게 c를 input 받는다
    road[a-1].append([-c, b-1, a-1])            # a섬에서 연결된 다리 [지나갈 수 있는 무게, 도착섬, 출발섬]정보를 append
    road[b-1].append([-c, a-1, b-1])            # b섬에서 연결된 다리 [지나갈 수 있는 무게, 도착섬, 출발섬]정보를 append

ans = [-1e9] * N                                # 해당 섬까지 들고갈 수 있는 금빼빼로의 수를 저장할 리스트 생성
visited = [0] * N                               # 섬의 방문 표시를 할 리스트 생성
tmp = [[-1e9, start-1, start-1]]                # tmp에 시작점을 넣고 리스트를 생성해서
while tmp:                                      # tmp가 빌때까지 반복한다
    cost, node, node2 = heapq.heappop(tmp)      # 무게, 도착섬, 시작섬 정보를 heappop해서 받은 후
    if visited[node] == 0:                      # 도착섬이 방문 전이라면
        visited[node] = 1                       # 방문표시를 하고
        if ans[node2] < cost:                   # 출발섬까지 들고갈 수 있는 무게보다 현재 다리의 무게가 작다면
            ans[node] = cost                    # 도착섬의 정보에 현재 다리 무게 정보를 저장하고
        else:                                   # 출발섬까지 들고갈 수 있는 무게보다 현재 다리의 무게가 작다면
            ans[node] = ans[node2]              # 도착섬의 정보에 출발 섬까지 저장된 무게를 저장한다
        if node == end - 1:                     # 도착섬이 도착점의 정보와 같아지면
            break                               # while문을 종료한다
        for r in road[node]:                    # 도착섬과 연결된 다리를 탐색해서
            if visited[r[1]] == 0:              # 다리의 끝이 방문 전이라면
                heapq.heappush(tmp, r)          # tmp에 heappush한다

if -ans[end-1] == 1e9:                          # 도착섬의 정보가 바뀌지 않았다면
    print(0)                                    # 0을 출력하고
else:                                           # 도착섬의 정보가 바뀌었다면
    print(-ans[end-1])                          # 가지고 갈 수 있는 금빼빼로의 수를 출력한다