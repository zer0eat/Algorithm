# 최단경로_BOJ1753

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
V, E = map(int, input().split())            # V 정점의 개수 / E 간선의 개수
start = int(input())                        # 시작점을 input 받고
road = dict()                               # 정점끼리 연결하는 선과 그 비용을 저장할 딕셔너리 생성
for e in range(E):                          # 간선의 개수를 반복해서
    a, b, c = map(int, input().split())     # a 시작점 b 도착점 c 비용을 input 받고
    if road.get(a) == None:                 # a가 key인 딕셔너리의 원소가 없을 때
        road[a] = [[c, b]]                  # a가 key일 때 value가 [[c,b]]인 원소를 생성한다
    else:                                   # a가 key인 딕셔너리의 원소가 있다면
        road[a].append([c, b])              # a가 key일 때 value에 [c,b]를 append

tmp = [[0, start]]                          # 가중치가 0이고 시작점을 넣은 리스트를 리스트에 넣어 생성하고
visited = [1e9]*(V+1)                       # 해당 노드까지의 비용을 저장할 리스트를 생성한다
while tmp:                                  # tmp가 빌때까지 반복해서
    c, b= heapq.heappop(tmp)                # tmp에서 heappop해서 c에 가중치 b에 도착 노드를 저장한다
    if visited[b] > c:                      # 만약 visited의 b에 저장된 기록이 가중치보다 크다면 
        visited[b] = c                      # visited[b]에 새로운 가중치를 저장하고
        if road.get(b) != None:             # b와 연결된 노드가 있다면
            for cost, node in road[b]:      # b가 key인 딕셔너리를 반복해서 cost와 node를 저장한다
                cost += c                   # cost에 tmp에서 pop한 가중치인 c를 더해주고
                if visited[node] > cost:    # visited의 b에 저장된 기록이 cost보다 크다면   
                    heapq.heappush(tmp, [cost, node])   # tmp에 [cost, node]를 heappush한다

for i in range(1, V+1):                     # 1부터 마지막 노드까지 반복해서
    if visited[i] == 1e9:                   # 해당 노드의 비용이 바뀌지 않은 상태라면
        print('INF')                        # INF를 출력하고
    else:                                   # 바뀌어있다면
        print(visited[i])                   # 해당 노드의 비용을 출력한다