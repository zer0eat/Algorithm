# 떡돌리기_BOJ20007

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, X, Y = map(int, input().split())                  # N 집의 수 / M 길의 수 / X 하루에 갈 수 있는 최대 거리 / Y 출발점
road = [[] for _ in range(N)]                           # 길의 정보를 저장할 리스트 생성
for _ in range(M):                                      # 길의 수를 반복해서
    a, b, c = map(int, input().split())                 #  a,b 집과 c 거리를 input 받고
    road[a].append([c, b])                              # a에 [거리, 연결 집] 정보를 append
    road[b].append([c, a])                              # b에 [거리, 연결 집] 정보를 append

def dijkstra(start):
    distance = [1e9] * N                                # 거리를 저장할 리스트를 생성하고
    distance[start] = 0                                 # start의 거리를 0으로 저장한다
    tmp = [[0, start]]                                  # tmp에 시작점을 넣고 리스트를 생성한 후
    while tmp:                                          # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)                 # 거리와 연결 집을 heappop한 후
        if cost > distance[node]:                       # cost가 저장된 거리보다 큰 경우에는
            continue                                    # continue 해서 넘어가고
        for r in road[node]:                            # 연결 집과 이어진 길을 반복해서
            cost2 = cost + r[0]                         # cost2에 현재 거리와 길의 거리를 더한 후
            if cost2 < distance[r[1]]:                  # cost2가 길의 도착지에 저장된 거리보다 작다면
                distance[r[1]] = cost2                  # 도착지의 거리를 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [cost2, 도착지 집]을 heappush한다
    return distance                                     # start에서 각 집까지 비용을 return

result = dijkstra(Y)                                    # 시작 집에서 도착 집까지 거리를 result에 저장한 후

for r in result:                                        # 거리 정보를 반복해서
    if r > X//2:                                        # 거리가 하루에 갈 수있는 최대 값의 반보다 크다면
        print(-1)                                       # 갈 수 없으므로 -1을 출력하고
        quit()                                          # quit 한다

result.sort()                                           # result를 오름차순으로 정렬하고
maxMove = 0                                             # 하루에 갈 수 있는 거리를 저장할 변수
day = 1                                                 # 걸리는 일 수를 저장할 변수
for i in range(N):                                      # 집의 수 만큼 반복해서
    if (maxMove + result[i])*2 <= X:                    # 현재 이동거리와 다음 이동거리의 합이 최대거리의 반보다 작다면
        maxMove = maxMove + result[i]                   # maxMove에 현재이동거리와 다음 이동거리의 합을 더해서 저장한다
    else:                                               # 만약 현재 이동거리와 다음 이동거리의 합이 최대거리의 반보다 크다면
        maxMove = result[i]                             # maxMove를 다음 이동거리로 초기화 해서 저장한 후
        day += 1                                        # 하루를 추가한다
print(day)                                              # 총 걸린 일수를 출력한다