# LostMap_BOJ16393

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                                            # 마을의 수를 input 받고
road = [list(map(int, input().split())) for _ in range(N)]                  # 마을과 마을이 연결된 거리 행렬을 input 받는다

ans = []                                                                    # 정답을 저장할 리스트를 생성하고 
tmp = [[0, 0, 0]]                                                           # [이동비용, 도착점, 시작점]을 넣은 tmp 리스트를 생성한다
visited = [0] * N                                                           # 방문 기록을 저장할 리스트를 생성하고
minCost = [1e9] * N                                                         # 최소 비용을 저장할 리스트를 생성하고
cnt = 0                                                                     # 방문 마을의 수를 저장할 변수를 생성한다
while cnt < N:                                                              # cnt가 N이 될 때까지 반복해서
    cost, node1, node2 = heapq.heappop(tmp)                                 # 비용, 도착점, 시작점을 heappop해서
    if visited[node1] == 0:                                                 # 도착점이 아직 방문 전이라면
        cnt += 1                                                            # 방문 마을의 수를 1 추가하고
        A = [node1, node2]                                                  # [도착점, 시작점]을 A에 저장한 후
        A.sort()                                                            # 오름차순 정렬한다
        ans.append(A)                                                       # ans에 A를 append하고
        visited[node1] = 1                                                  # 도착점을 방문표시한다
        for r in range(N):                                                  # 마을의 수를 반복해서
            if node1 != r:                                                  # 도착점과 같은 마을이 아닐 경우에
                if visited[r] == 0:                                         # 해당 마을이 방문 전이라면
                    if minCost[r] > road[node1][r]:                         # 현재 저장된 최소 비용과 비교해서 새로운 길이 더 비용이 적다면
                        minCost[r] = road[node1][r]                         # 최소비용을 현재 길의 비용으로 저장하고
                        heapq.heappush(tmp, [road[node1][r], r, node1])     # tmp에 [비용, 해당마을, 도착점]을 heappush한다

ans.sort()                                                                  # 정답을 오름차순으로 정렬해서
for a in range(1, N):                                                       # N-1개의 간선을 반복해서
    x, y = ans[a]                                                           # 출발점과 도착점을 x, y에 저장하고
    print(x+1, y+1)                                                         # 출발점과 도착점을 출력한다