# 서강그라운드_BOJ14938

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, R = map(int, input().split())                     # N 지역의수 / M 최대 이동거리 / R 연결된 길의수
item = list(map(int, input().split()))                  # 각 지역마다 가지고 있는 아이템의 수를 리스트로 input 받고
road = [[] for _ in range(N)]                           # 길의 정보를 저장할 리스트 생성

for _ in range(R):                                      # 연결된 길의 수를 반복해서
    a, b, c = map(int, input().split())                 # a,b 지역 c 비용을 input 받는다
    road[a-1].append([c, b-1])                          # a지역에서 갈 수 있는 길의 정보인 [비용, 연결된 지역]을 append 한다
    road[b-1].append([c, a-1])                          # b지역에서 갈 수 있는 길의 정보인 [비용, 연결된 지역]을 append 한다

def dijkstra(start):
    distance = [1e9]*N                                  # 각 지역까지의 거리를 저장할 리스트 생성
    distance[start] = 0                                 # 출발 마을까지 비용을 0으로 저장
    tmp = [[0, start]]                                  # 시작점을 넣은채로 tmp 리스트 생성
    while tmp:                                          # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # 비용과 다음 지역 정보를 heappop해서 꺼낸다
        if cost < distance[node]:                       # 저장된 다음 지역까지 비용보다 cost가 더 크다면 최소비용이 아니므로
            continue                                    # continue로 넘어간다
        for r in road[node]:                            # 연결된 지역과 연결된 도로를 반복해서
            cost2 = cost + r[0]                         # 현재 비용과 연결된 도로 비용을 더한 값을 cost2로 저장하고
            if cost2 < distance[r[1]]:                  # cost2가 연결된 도로의 도착지까지 저장된 비용보다 작을 경우
                distance[r[1]] = cost2                  # cost2로 갱신하여 저장하고
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [갱신된 비용, 도착지역]을 heapppush 한다
    return distance                                     # while문이 종료되면 distance 리스트를 return 한다

ans = 0                                                 # 최대 아이템을 저장할 변수를 생성
for i in range(N):                                      # 지역의 수를 반복해서
    result = dijkstra(i)                                # i지역에서 출발 했을 때 이동비용을 dijkstra를 이용해 구한 후 리스트로 저장
    tmp = 0                                             # i지역에서 출발 했을 때 얻을 수 있는 아이템을 저장할 변수 생성
    for r in range(N):                                  # 지역의 수를 반복해서
        if result[r] <= M:                              # 해당 지역까지 거리가 M 이하라면
            tmp += item[r]                              # 아이템을 tmp에 더한다
    else:                                               # 모든 지역을 반복했을 때
        if ans < tmp:                                   # ans보다 tmp가 더 크다면
            ans = tmp                                   # 최대 아이템 수를 tmp로 바꿔 저장한다
print(ans)                                              # 최대 아이템 수를 출력한다