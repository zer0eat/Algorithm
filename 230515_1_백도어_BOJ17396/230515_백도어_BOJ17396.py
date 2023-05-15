# 백도어_BOJ17396

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                    # N 분기점 / M 경로
road = [[] for _ in range(N)]                       # 경로의 정보를 저장할 리스트 생성
vision = list(map(int, input().split()))            # 시야 위치를 저장할 리스트 생성
for _ in range(M):                                  # 경로의 수를 반복해서
    a, b, c = map(int, input().split())             # a,b 분기점의 정보와 c 걸리는 시간을 받아온다
    a, b = min(a, b), max(a, b)                     # a와 b를 순서대로 정렬한 후
    if b != N-1 and (vision[a] or vision[b]):       # b가 도착지가 아니면서 a,b 둘 중 하나가 시야가 있다면
        pass                                        # 패스
    else:                                           # b가 4거나 둘다 시야가 없는 경우에는
        road[a].append([c, b])                      # road a인덱스에 [시간, 연결 분기점] 정보를 append
        road[b].append([c, a])                      # road b인덱스에 [시간, 연결 분기점] 정보를 append

def dijkstra(start):
    distance = [100000 * 100000 + 1] * N            # 분기점 별 걸리는 시간을 저장할 변수 생성
    distance[start] = 0                             # 시작 분기점을 0으로 저장
    tmp = [[0, start]]                              # 시작 분기점을 넣고 tmp 생성
    while tmp:                                      # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)             # cost와 node를 heappop해서
        if cost > distance[node]:                   # cost가 현재 저장된 이동시간보다 크다면
            continue                                # continur
        for r in road[node]:                        # node 분기점과 연결된 경로를 반복해서
            cost2 = cost + r[0]                     # cost2에 현재 비용과 경로를 이동하는데 드는 시간을 더해 저장한다
            if cost2 < distance[r[1]]:              # cost2가 현재 저장된 시간보다 적게 걸리는 경우에는
                distance[r[1]] = cost2              # distance[r[1]]을 cost2로 저장하고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [cost2, 경로의 연결 분기점]을 heappush한다
    return distance                                 # 출발점에서 각 분기점까지 걸리는 시간을 return

result = dijkstra(0)[-1]                            # 넥서스까지 걸리는 시간을 구해서 저장한다
if result == 100000 * 100000 + 1:                   # 넥서스에 도달할 수 없어서 걸리는 시간을 구할 수 없다면
    print(-1)                                       # -1 을 출력하고
else:                                               # 넥서스에 도달할 수 있어서 걸리는 시간이 나온다면
    print(result)                                   # 결과를 출력한다