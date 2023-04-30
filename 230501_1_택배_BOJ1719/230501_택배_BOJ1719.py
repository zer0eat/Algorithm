# 택배_BOJ1719

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 집하장의 수 / M 집하장으로 가는 경로의 수
road = [[] for _ in range(N)]               # 집하장의 경로를 저장할 리스트 생성
for _ in range(M):                          # 경로의 수를 반복해서
    a, b, c = map(int, input().split())     # a,b 집하장과 c 걸리는 시간을 input 받는다
    road[a-1].append([c, b-1, a-1])         # a 집하장에서 이동할 수 있는 곳을 [비용, 연결 집하장]을 append
    road[b-1].append([c, a-1, b-1])         # b 집하장에서 이동할 수 있는 곳을 [비용, 연결 집하장]을 append

def dijkstra(start):
    distance = [1e9] * N                    # 집하장까지 이동 시간을 저장할 리스트 생성
    ans = [-1] * N                          # 집하장 이동 시 가장 먼저 이동하는 집하장을 저장할 리스트 생성
    distance[start] = 0                     # start 집하장의 비용을 0으로 저장하고
    ans[start] = '-'                        # start 집하장까지 이동할 때 처음 지나는 집하장을 - 로 저장한다
    tmp = [[0, start, start]]               # tmp에 [시작비용, 시작점, 연결집하장]을 넣고 리스트 생성
    while tmp:                              # tmp가 빌 때까지 반복해서
        cost, node, stnode = heapq.heappop(tmp) # 비용, 연결된 집하장, 처음 연결된 집하장을 heappop 한다
        if cost > distance[node]:           # heappop한 비용이 현재 저장된 비용보다 크다면
            continue                        # continue한다
        for r in road[node]:                # 연결된 집하장과 연결된 경로를 반복해서
            cost2 = cost + r[0]             # cost2에 집하장까지의 비용과 연결된 경로의 비용을 더한 값을 저장하고
            if cost2 < distance[r[1]]:      # cost2가 현재 저장된 r[1] 집하장까지 비용보다 작다면
                distance[r[1]] = cost2      # r[1] 집하장의 비용을 cost2로 저장한다
                if r[2] == start:           # 처음 연결된 집하장이 start와 같다면
                    stnode = r[1]           # 처음 연결된 집하장을 연결된 집하장으로 변경한다
                ans[r[1]] = stnode + 1      # r[1] 노드로 이동하기 위해 처음 이동해야하는 집하장을 저장하고
                heapq.heappush(tmp, [cost2, r[1], stnode])  # [비용, 이동할 집하장, 이동하기 위해 처음 지나가는 집하장]을 heappush
    return ans                              # 처음 이동해야하는 집하장 리스트를 return

for i in range(N):                          # 집하장을 반복해서
    print(*dijkstra(i))                     # 해당 집하장에서 최단경로로 이동하기 위해 연결된 가장 먼저 지나가는 집하장을 출력한다