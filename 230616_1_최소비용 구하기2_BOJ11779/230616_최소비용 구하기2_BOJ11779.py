# 최소비용 구하기2_BOJ11779

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
    a, b, c = map(int, input().split())             # a, b 출발, 도착마을과 c 버스의 비용을 input
    road[a-1].append([c, b-1, a-1])                 # a-1 마을에서 출발했을 때 버스 정보 [비용, 도착마을, 출발마을]을 append
S, E = map(int, input().split())                    # 구하고자하는 S 출발마을 E 도착마을을 input

def dijkstra(start, end):
    distance = [1e9] * N                            # 비용정보를 저장할 리스트를 생성하고
    distance[start] = 0                             # 출발지를 0으로 바꾼다
    tmp = [[0, start, start]]                       # tmp에 시작점을 넣고 리스트를 생성한 후
    route = [[] for _ in range(N)]                  # 해당 마을에 최소비용으로 도착하기 위한 노선을 저장할 리스트 생성
    while tmp:                                      # tmp가 빌 때까지 반복한다
        cost, node, node2 = heapq.heappop(tmp)      # 비용과 연결 도시를 heappop한 후
        if distance[node] < cost:                   # cost가 저장된 비용보다 큰 경우
            continue                                # continue
        for r in road[node]:                        # 연결 도시에서 출발하는 버스노선을 반복해서
            cost2 = cost + r[0]                     # cost2에 현재 비용과 버스노선의 비용을 더한 후
            if distance[r[1]] > cost2:              # cost2가 버스 노선의 도착지에 저장된 비용보다 작다면
                distance[r[1]] = cost2              # 도착지의 비용을 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1], r[2]])  # tmp에 [cost2, 도착 도시, 출발 도시]를 heappush한다
                route[r[1]] = [r[1], r[2]]          # route리스트의 도착마을 인덱스에 [도착마을, 출발마을]을 저장한다

    ans = [end + 1]                                 # 노선 정보를 저장할 리스트에 도착지를 넣고 생성한 후
    tmp = end                                       # tmp에 도착지를 저장한다
    while 1:                                        # break가 나올때까지 반복해서
        if route[tmp][1] == start:                  # 현재 route의 출발지가 start와 같을 때
            ans.append(route[tmp][1] + 1)           # ans에 최초 출발지를 append 하고
            break                                   # while문을 break
        else:                                       # 현재 route의 출발지가 start와 다를 때
            ans.append(route[tmp][1] + 1)           # ans에 현재 지점에 도착하기 위한 출발지를 append하고
            tmp = route[tmp][1]                     # 현재 출발지를 tmp로 저장한다
    ans.reverse()                                   # while문이 끝났다면 ans를 뒤집어서 출발에서 도착순서로 바꿔준 후
    answer = [distance[end], len(ans), ans]         # answer 리스트에 [최소비용, 출발지에서 도착지로 가는 동안 들리는 마을의 수, 마을의 경로]를 저장
    return answer                                   # answer를 return

answer = dijkstra(S-1, E-1)                         # answer에 출발지와 도착지 정보를 dijkstra 함수를 통해 결과를 구한 후
for a in range(3):                                  # 3개의 원소를 반복해서
    if a == 2:                                      # 2번 원소인 경우에는
        print(*answer[a])                           # 리스트를 없에서 원소들만 출력한다
    else:                                           # 0,1 번 원소인 경우에는
        print(answer[a])                            # 출력하고