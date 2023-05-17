# RUN_BOJ18402

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                        # 감옥의 수
E = int(input())                                        # 출구번호
T = int(input())                                        # 타이머
M = int(input())                                        # 길의 수
road = [[] for _ in range(N)]                           # 길의 정보를 저장할 리스트 생성
for _ in range(M):                                      # 길의 수를 반복해서
    a, b, c = map(int, input().split())                 #  a,b 감옥과 c 거리를 input 받고
    road[a-1].append([c, b-1])                          # a에 [거리, 연결 감옥] 정보를 append

def dijkstra(start):
    distance = [1e9] * N                                # 거리를 저장할 리스트를 생성하고
    distance[start] = 0                                 # start의 거리를 0으로 저장한다
    tmp = [[0, start]]                                  # tmp에 시작점을 넣고 리스트를 생성한 후
    while tmp:                                          # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)                 # 거리와 연결 감옥을 heappop한 후
        if cost > distance[node]:                       # cost가 저장된 거리보다 큰 경우에는
            continue                                    # continue 해서 넘어가고
        for r in road[node]:                            # 연결 감옥과 이어진 길을 반복해서
            cost2 = cost + r[0]                         # cost2에 현재 거리와 길의 거리를 더한 후
            if cost2 < distance[r[1]]:                  # cost2가 길의 도착지에 저장된 거리보다 작다면
                distance[r[1]] = cost2                  # 도착지의 거리를 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [cost2, 도착지 감옥]을 heappush한다
    return distance[E-1]                                # start에서 출구까지 비용을 return

ans = 0                                                 # 탈출한 사람의 수를 저장할 변수 생성
for a in range(N):                                      # 수감자를 반복해서
    if dijkstra(a) <= T:                                # 탈출할 때 걸리는 거리가 T 이하라면
        ans += 1                                        # ans에 1을 더해준다
print(ans)                                              # 총 탈출한 수감자를 출력한다