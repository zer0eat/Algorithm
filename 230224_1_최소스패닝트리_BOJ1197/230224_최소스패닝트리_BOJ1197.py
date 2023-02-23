# 최소스패닝트리_BOJ1197

# input.txt
import sys
import heapq
sys.stdin = open('input.txt')

# input 받기
V, E = map(int, sys.stdin.readline().split())           # V 노드의수 / E 간선의수
road = [[] for _ in range(V)]                           # road 리스트와 각 인덱스가 출발 노드가 되는 리스트내 리스트를 생성한다

for _ in range(E):                                      # 간선의 수를 반복해서
    a, b, c = map(int, sys.stdin.readline().split())    # a,b 두 노드와 c 가중치를 input 받는다
    road[a-1].append([c, b-1])                          # a-1을 출발지로 설정하고 [가중치, 도착지(b-1)]를 append해서 길을 저장한다
    road[b-1].append([c, a-1])                          # 반대로 b-1을 출발지로 설정하고 [가중치, 도착지(a-1)]를 append해서 길을 저장한다

visited = [0]*V                                         # 각 노드의 방문표시를 하는 리스트를 생성하고

line = [[0,1]]                                          # 최소 가중치부터 탐색을 하기 위해 리스트를 생성하고 시작점([가중치 없음, 시작점])을 넣는다

ans = 0                                                 # 최소 가중치를 저장할 변수를 생성하고
cnt = 0                                                 # 방문한 노드의 수를 저장할 변수를 생성한다
while cnt < V:                                          # 모든 노드를 방문할 때까지 반복해서
    c, town = heapq.heappop(line)                       # line 리스트에서 가중치가 가장 작은 수를 heappop한다
    if visited[town] == 0:                              # pop한 길의 도착지가 방문 전이라면
        visited[town] = 1                               # 방문표시를 해주고
        cnt += 1                                        # 방문한 노드의 수를 1 추가한다
        ans += c                                        # 최소 가중치에 가중치를 추가하고
        for r in road[town]:                            # 도착지에서 다음으로 갈 수 있는 길을 반복해서
            heapq.heappush(line, r)                     # line에 heappush한다

print(ans)                                              # 모든 노드의 방문을 마쳤다면 ans를 출력한다