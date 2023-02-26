# 도시분할계획_BOJ1647

# input.txt
import sys
import heapq
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, sys.stdin.readline().split())           # N 집의 개수 / M 길의 개수
road = dict()                                           # 길을 저장하기 위한 딕셔너리 생성

for _ in range(M):                                      # 길의 수를 반복해서
    a, b, c = map(int, sys.stdin.readline().split())    # a,b 집의 위치와 c 유지비를 input 받는다
    if road.get(a-1) == None:                           # road 딕셔너리에 key값이 a-1인 요소가 없다면
        road[a-1] = [[c, b-1]]                          # a-1이 key이고 [c, b-1]가 value인 요소를 생성하고
    else:                                               # road 딕셔너리에 key값이 a-1인 요소가 있다면
        road[a-1].append([c, b-1])                      # a-1이 key인 요소의 value에 [c, b-1]를 append한다
    if road.get(b-1) == None:                           # road 딕셔너리에 key값이 b-1인 요소가 없다면
        road[b-1] = [[c, a-1]]                          # b-1이 key이고 [c, a-1]가 value인 요소를 생성하고
    else:                                               # road 딕셔너리에 key값이 b-1인 요소가 있다면
        road[b-1].append([c, a-1])                      # b-1이 key인 요소의 value에 [c, a-1]를 append한다

   
visited = [0]*N                                         # 각 집의 방문표시를 하는 리스트를 생성하고
line = [[0,0]]                                          # 최소 가중치부터 탐색을 하기 위해 리스트를 생성하고 시작점([가중치 없음, 시작점])을 넣는다

ans = 0                                                 # 모든 집을 최소 유지비로 연결했을 때 값을 저장하기 위한 변수 생성
cnt = 0                                                 # 방문한 집의 수를 저장할 변수를 생성한다
maxcost = 0                                             # 집을 연결하는 유지비 중 최대값을 저장하기 위한 변수생성
while cnt < N:                                          # 모든 집을 방문할 때까지 반복해서
    c, end = heapq.heappop(line)                        # line 리스트에서 유지비가 가장 작은 수를 heappop한다
    if visited[end] == 0:                               # pop한 길의 도착지가 방문 전이라면
        visited[end] = 1                                # 방문표시를 해주고
        cnt += 1                                        # 방문한 집의 수를 1 추가한다
        if maxcost < c:                                 # 도착지까지 유지비가 현재 최대값보다 크다면
            maxcost = c                                 # 현재 최대값을 c 유지비로 바꿔 저장한다
        ans += c                                        # ans에 유지비를 추가하고
        for r in road[end]:                             # 도착지에서 다음으로 갈 수 있는 길을 반복해서
            if visited[r[1]] == 0:                      # 다음 도착지가 방문 전이라면
                heapq.heappush(line, r)                 # line에 heappush한다

print(ans-maxcost)                                      # 총 유지비에서 최대 유지비를 빼서 두개로 분리된 마을의 유지비를 출력한다