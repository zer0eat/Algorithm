# Bronze Cow Party_BOJ6248

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, X = map(int, input().split())                     # N 농장의 수 / M 길의 수 / X 파티 장소
road = [[] for _ in range(N)]                           # 길의 정보를 저장할 리스트 생성
for _ in range(M):                                      # 길의 수를 반복해서
    a, b, c = map(int, input().split())                 # a, b 농장의 정보 c 이동 비용을 input 받고
    road[a-1].append([c, b-1])                          # a 농장에서 이동할 수 있는 곳을 [비용, 연결 농장]을 append
    road[b-1].append([c, a-1])                          # b 농장에서 이동할 수 있는 곳을 [비용, 연결 농장]을 append

def dijkstra(start):
    distance = [1e9] * N                                # 농장까지 이동 시간을 저장할 리스트 생성
    distance[start] = 0                                 # start 농장까지 이동 비용을 0으로 저장
    tmp = [[0, start]]                                  # tmp에 [시작비용, 시작점]을 넣고 리스트 생성
    while tmp:                                          # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # tmp에서 비용과 연결 농장 정보를 heappop한다
        if cost > distance[node]:                       # cost가 현재 저장된 농장 이동비용보다 크다면
            continue                                    # continue
        for r in road[node]:                            # 이동한 농장에서 연결된 길을 반복해서
            cost2 = cost + r[0]                         # 현재까지 이동비용과 연결된 길의 비용을 더한값을 cost2에 저장하고
            if cost2 < distance[r[1]]:                  # cost2가 현재 저장된 비용보다 작다면
                distance[r[1]] = cost2                  # cost2를 저장비용을 바꿔 저장하고
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [이동비용, 길의 도착지]로 heappush
    return distance                                     # distance를 return한다

result = dijkstra(X-1)                                  # 출발점에서 dijkstra로 각 농장까지 비용을 구해 result에 저장하고
print(max(result)*2)                                    # 파티를 중지하는 시간을 출력한다