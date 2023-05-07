# 민준이와 마산 그리고 건우_BOJ18223

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
V, E, P = map(int, input().split())                 # V 정점의 수 / E 간선의 수 / P 건우의 위치
road = [[] for _ in range(V)]                       # 간선의 경로를 저장할 리스트 생성
for _ in range(E):                                  # 간선의 수를 반복해서
    a, b, c = map(int, input().split())             # a, b 정점의 정보 c 거리를 input 받고
    road[a-1].append([c, b-1])                      # a 정점에서 이동할 수 있는 곳을 [거리, 연결 정점]을 append
    road[b-1].append([c, a-1])                      # b 정점에서 이동할 수 있는 곳을 [거리, 연결 정점]을 append

def dikstra(start):
    ans = [0] * V                                   # 정점까지 이동 시 건우를 만나는지 여부를 저장할 리스트 생성
    distance = [1e9] * V                            # 정점까지 이동 시간을 저장할 리스트 생성
    distance[start] = 0                             # start 정점까지 이동 비용을 0으로 저장
    if P == 1:                                      # 시작점에 건우가 있다면
        tmp = [[0, start, 1]]                       # tmp에 [시작거리, 시작점, 1]을 넣고 리스트 생성
        ans[0] = 1                                  # ans의 시작점에 1로 표시한다
    else:                                           # 시작점에 건우가 없다면
        tmp = [[0, start, 0]]                       # tmp에 [시작거리, 시작점, 0]을 넣고 리스트 생성
    while tmp:                                      # tmp가 빌때까지 반복해서
        cost, node, flag = heapq.heappop(tmp)       # tmp에서 거리와 연결 정점 정보, 건우를 만났는지 여부를 heappop한다
        if cost > distance[node]:                   # cost가 현재 저장된 정점 거리보다 크다면
            continue                                # continue
        for r in road[node]:                        # 이동한 정점에서 연결된 간선을 반복해서
            cost2 = cost + r[0]                     # 현재까지 거리와 연결된 간선의 거리를 더한값을 cost2에 저장하고
            if cost2 < distance[r[1]]:              # cost2가 현재 저장된 거리보다 작다면
                distance[r[1]] = cost2              # cost2를 최소 이동 거리로 바꿔 저장하고
                if r[1] == P-1:                     # 이동한 정점이 건우가 있는 정점이라면
                    ans[r[1]] = 1                   # ans의 r[1]에 건우를 구출 표시를 한 후
                    heapq.heappush(tmp, [cost2, r[1], ans[r[1]]])   # tmp에 [이동거리, 간선의 도착지, 건우 만남]으로 heappush
                else:                               # 이동한 정점이 건우가 있는 정점이 아니라면
                    ans[r[1]] = flag                # ans의 r[1]에 flag로 표시를 한 후
                    heapq.heappush(tmp, [cost2, r[1], flag])        # tmp에 [이동거리, 간선의 도착지, flag]으로 heappush
            elif cost2 == distance[r[1]] and flag == 1:             # cost2가 현재 저장된 거리와 같을 때 건우를 구출할 수 있다면
                    ans[r[1]] = 1                   # ans의 r[1]에 건우를 구출 표시를 한 후
                    heapq.heappush(tmp, [cost2, r[1], 1])           # tmp에 [이동거리, 간선의 도착지, 건우 만남]으로 heappush
    return ans[-1]                                  # 도착지까지 이동했을 때 건우를 만났는지 여부를 return

result = dikstra(0)                                 # 출발점에서 dijkstra로 도착 정점까지 이동했을 때 건우를 만났는지 여부를 result에 저장하고 
if result:                                          # result가 1이면
    print('SAVE HIM')                               # SAVE HIM을 출력
else:                                               # result가 0이면
    print('GOOD BYE')                               # GOOD BYE를 출력

