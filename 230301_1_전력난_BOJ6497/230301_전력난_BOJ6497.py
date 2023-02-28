# 전력난_BOJ6497

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
while 1:                                        # M과 N이 0일 때까지 반복해서
    M, N = map(int, input().split())            # M 집의 수 / N 길의 수
    if M == 0 and N == 0:                       # M과 N이 0이라면
        quit()                                  # 종료한다
    road = dict()                               # 길의 정보를 저장할 딕셔너리를 생성하고
    maxans = 0                                  # 모든 길의 비용을 저장할 변수를 생성한다
    for _ in range(N):                          # 길의 수를 반복해서
        x,y,z = map(int, input().split())       # x 시작집 / y 도착집 / z 비용을 input 받고
        maxans += z                             # maxans에 비용을 더해준다
        if road.get(x) == None:                 # 만약 x가 key인 값이 없다면
            road[x] = [[z,y]]                   # x가 key이고 [z,y]가 value인 요소를 만든다
        else:                                   # 만약 x가 key인 값이 있다면
            road[x].append([z,y])               # x가 key인 value에 [z,y]를 append한다
        if road.get(y) == None:                 # 만약 y가 key인 값이 없다면
            road[y] = [[z,x]]                   # y가 key이고 [z,x]가 value인 요소를 만든다
        else:                                   # 만약 y가 key인 값이 있다면
            road[y].append([z,x])               # y가 key인 value에 [z,x]를 append한다

    visited = [0]*M                             # 집의 방문여부를 저장할 리스트를 생성한다
    ans = 0                                     # 정답을 저장할 변수를 생성한다
    cnt = 0                                     # 방문한 집의수를 저장할 변수를 생성한다
    line = [[0,0]]                              # 시작점을 저장한 리스트를 생성한다

    while cnt < M:                              # 모든집을 방문할 때까지 반복해서
        cost, end = heapq.heappop(line)         # line 리스트에서 비용이 최소인 값을 heappop해서 비용과 도착지를 저장한다
        if visited[end] == 0:                   # 도착지가 방문 전이라면
            visited[end] = 1                    # 도착지를 visited에 방문표시를 해주고
            cnt += 1                            # 방문한 집의 수를 1 추가한 후
            ans += cost                         # 최소비용을 저장하는 변수에 현재 길의 비용을 추가한다
            for r in road[end]:                 # 도착지에서 갈 수 있는 집들을 반복해서
                if visited[r[1]] == 0:          # 그 다음 도착지가 방문 전이라면 
                    heapq.heappush(line, r)     # line 리스트에 heappush한다

    print(maxans-ans)                           # 전체비용에서 최소비용을 뺀 값을 출력한다