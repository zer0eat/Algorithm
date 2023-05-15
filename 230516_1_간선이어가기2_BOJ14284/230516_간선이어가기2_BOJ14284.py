# 간선이어가기2_BOJ14284

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                    # N 정점의 수 / M 간선의 수
road = [[] for _ in range(N)]                       # 간선의 정보를 저장할 리스트 생성
for _ in range(M):                                  # 간선의 수를 반복해서
    a, b, c = map(int, input().split())             # a,b 정점과 c 비용을 input 받고
    road[a-1].append([c, b-1])                      # a-1에 [비용, 연결정점] 정보를 append
    road[b-1].append([c, a-1])                      # b-1에 [비용, 연결정점] 정보를 append
start, end = map(int, input().split())              # 시작점과 도착점 정보를 input 받고

def dijkstra(start):
    distance = [1e9] * N                            # 비용을 저장할 리스트를 생성하고
    distance[start] = 0                             # start의 비용을 0으로 저장한다
    tmp = [[0, start]]                              # tmp에 시작점을 넣고 리스트를 생성한 후
    while tmp:                                      # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)             # 비용과 연결 정점을 heappop한 후
        if cost > distance[node]:                   # cost가 저장된 비용보다 큰 경우에는
            continue                                # continue 해서 넘어가고
        for r in road[node]:                        # 연결 정점과 이어진 간선을 반복해서
            cost2 = cost + r[0]                     # cost2에 현재 비용과 간선을 지나는 비용을 더한 후
            if cost2 < distance[r[1]]:              # cost2가 간선의 도착지에 저장된 비용보다 작다면
                distance[r[1]] = cost2              # 도착지의 비용을 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [cost2, 도착지 정점]을 heappush한다
    return distance                                 # start에서 각 정점까지 비용을 return

result = dijkstra(start- 1)[end -1]                 # 시작점에서 도착점까지 비용을 result에 저장한 후
print(result)                                       # 출력한다