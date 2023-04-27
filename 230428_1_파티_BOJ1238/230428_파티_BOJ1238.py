# 파티_BOJ1238

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, X = map(int, input().split())                     # N 학생의 수 / M 연결된 길의 수 / X 파티를 하는 마을 번호
road = [[] for _ in range(N+1)]                         # 연결된 길을 저장할 리스트 생성

for i in range(M):                                      # 연결된 길의 수를 반복해서
    a, b, c = map(int, input().split())                 # a,b 마을과 c 비용을 input 받는다
    road[a].append([c, b])                              # a마을에서 갈 수 있는 길의 정보인 [비용, 연결된 마을]을 append 한다

def dijkstra(start):                                    
    distance = [1e9] *(N+1)                             # 각 마을 까지의 거리를 저장할 리스트 생성
    tmp = [[0, start]]                                  # 시작점을 넣은채로 tmp 리스트 생성
    distance[start] = 0                                 # 출발 마을까지 비용을 0으로 저장
    while tmp:                                          # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # 비용과 다음 마을 정보를 heappop해서 꺼낸다
        if distance[node] < cost:                       # 저장된 다음 마을까지 비용보다 cost가 더 크다면 최소비용이 아니므로
            continue                                    # continue로 넘어간다
        for r in road[node]:                            # 연결된마을과 연결된 도로를 반복해서
            cost2 = cost + r[0]                         # 현재 비용과 연결된 도로 비용을 더한 값을 cost2로 저장하고
            if cost2 < distance[r[1]]:                  # cost2가 연결된 도로의 도착지까지 저장된 비용보다 작을 경우
                distance[r[1]] = cost2                  # cost2로 갱신하여 저장하고
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [갱신된 비용, 도착마을]을 heapppush 한다
    return distance                                     # while문이 종료되면 distance 리스트를 return 한다

goHome = dijkstra(X)                                    # 파티장에서 집에가는 비용을 goHome에 저장
ans = 0                                                 # 왕복비용 중 가장 큰 비용을 저장할 변수 생성
for i in range(1, N+1):                                 # 1부터 N까지 마을을 반복해서
    goParty = dijkstra(i)                               # 파티장에 갈 비용을 구하고
    tmp = goParty[X] + goHome[i]                        # tmp에 가는 비용과 오는 비용의 합을 저장한후
    if tmp > ans:                                       # ans보다 tmp가 더 큰 경우에
        ans = tmp                                       # tmp를 ans에 저장한다
print(ans)                                              # ans의 최고 비용을 출력한다