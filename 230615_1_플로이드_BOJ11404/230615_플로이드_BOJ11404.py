# 플로이드_BOJ11404

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                    # 도시의 수
M = int(input())                                    # 버스의 수
road = [[] for _ in range(N)]                       # 버스의 노선 정보를 저장할 리스트 생성
for _ in range(M):                                  # 버스의 수를 반복해서
    a, b, c = map(int, input().split())             # a, b  버스의 수를 input 받고 c 버스의 비용을 input
    road[a-1].append([c, b-1])                      # a-1 마을에서 출발했을 때 버스 정보 [비용, 도착마을]을 append

def dijkstra(start):
    distance = [1e9] * N                            # 비용정보를 저장할 리스트를 생성하고
    distance[start] = 0                             # 출발지를 0으로 바꾼다
    tmp = [[0, start]]                              # tmp에 시작점을 넣고 리스트를 생성한 후
    while tmp:                                      # tmp가 빌 때까지 반복한다
        cost, node = heapq.heappop(tmp)             # 비용과 연결 도시를 heappop한 후
        if distance[node] < cost:                   # cost가 저장된 비용보다 큰 경우
            continue                                # continue
        for r in road[node]:                        # 연결 도시에서 출발하는 버스노선을 반복해서
            cost2 = cost + r[0]                     # cost2에 현재 비용과 버스노선의 비용을 더한 후
            if distance[r[1]] > cost2:              # cost2가 버스 노선의 도착지에 저장된 비용보다 작다면
                distance[r[1]] = cost2              # 도착지의 비용을 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [cost2, 도착 도시]를 heappush한다
    return distance                                 # 비용정보 리스트를 return

for i in range(N):                                  # 출발지를 반복해서
    A = dijkstra(i)                                 # 다른 마을까지 최소비용 리스트를 A에 저장하고
    for j in range(N):                              # 출발지를 반복해서
        if A[j] == 1e9:                             # 도착지까지 도달할 수 없어 비용이 갱신되지 않았다면
            A[j] = 0                                # 비용을 0으로 바꾼 후
    print(*A)                                       # 도시별 비용정보를 출력한다