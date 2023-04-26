# 최소비용구하기_BOJ1916

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                            # 도시의 개수
M = int(input())                            # 버스의 개수
road = [[] for _ in range(N + 1)]           # 도시를 이동하는 버스의 경로를 저장할 리스트 생성

for i in range(M):                          # 버스의 개수를 반복해서
    a, b, c = map(int, input().split())     # a,b 도시와 c 비용을 input 받는다
    road[a].append([c, b])                  # road의 a 원소에 [비용, 연결 도시]를 append

start, end = map(int, input().split())      # 시작점과 도착점을 input 받고

visited = [0] * (N + 1)                     # 방문표시를 할 리스트와
distance = [1e9] * (N + 1)                  # 거리를 저장할 리스트 생성

def dijkstra(start):
    tmp = [[0, start]]                      # tmp에 시작점[[0, 시작마을]]을 넣고 생성
    distance[start] = 0                     # 시작마을 비용을 0으로 설정하고
    while tmp:                              # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)     # tmp에서 heappop해서 cost와 node를 꺼내 저장한 후
        if distance[node] < cost:           # cost가 연결된 마을 node의 비용보다 크다면
            continue                        # 바꿀 필요가 없으므로 continue 한다
        for r in road[node]:                # 연결된 마을의 버스 노선을 탐색해서
            cost2 = cost + r[0]             # node마을 까지 비용과 그다음 버스 노선을 더해 cost2로 저장한 후
            if cost2 < distance[r[1]]:      # cost2가 node랑 연결된 마을까지 비용보다 작다면
                distance[r[1]] = cost2      # node랑 연결된 마을의 비용을 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [비용, 연결도시]를 heappush

dijkstra(start)                             # 다익스트라 함수에 시작점을 넣고
print(distance[end])                        # 시작점에서 끝점까지 가는 최소 비용을 출력한다