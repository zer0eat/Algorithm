# Autostrady_BOJ8549

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 도시의 수 / M 도로의 수
road = dict()                               # 도로 정보를 저장할 딕셔너리 생성

for _ in range(M):                          # 도로의 수만큼 반복해서
    a, b, c = map(int, input().split())     # a, b 도시를 연결할 때 드는 비용 c를 input 받는다
    if road.get(a-1) == None:               # a 도시와 연결된 도시가 하나도 없을 때
        road[a-1] = [[c, b-1]]              # 딕셔너리에 a가 키일 때 [[비용 , 연결할 도시]] value를 생성한다
    else:                                   # a 도시가 key인 value가 존재한다면
        road[a-1].append([c, b-1])          # 딕셔너리에 a가 키일 때 [비용 , 연결할 도시]을 append 한다
    if road.get(b-1) == None:               # b 도시와 연결된 도시가 하나도 없을 때
        road[b-1] = [[c, a-1]]              # 딕셔너리에 b가 키일 때 [[비용 , 연결할 도시]] value를 생성한다
    else:                                   # b 도시가 key인 value가 존재한다면
        road[b-1].append([c, a-1])          # 딕셔너리에 b가 키일 때 [비용 , 연결할 도시]을 append 한다

ans = []                                    # 연결 비용을 저장할 리스트를 생성하고
visited = [0] * N                           # 방문 확인을 할 리스트를 생성한다
tmp = [[0, 0]]                              # 연결할 도로 정보를 저장할 리스트를 생성한 후 출발점을 넣는다
while tmp:                                  # tmp가 빌때까지 반복해서
    cost, node = heapq.heappop(tmp)         # tmp에서 heappop하여 cost와 연결할 다음 도시를 변수에 저장한다
    if visited[node] == 0:                  # 연결할 도시가 방문 전이라면
        visited[node] = 1                   # 방문표시를 하고
        ans.append(cost)                    # 연결 비용을 ans에 append 한다
        for r in road[node]:                # 연결할 도시와 연결된 도시를 반복해서
            if visited[r[1]] == 0:          # 연결된 도시가 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush한다
print(max(ans))                             # 도로 건설 비용 중 가장 비싼 비용 하나를 출력한다