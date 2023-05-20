# Underground Cables_BOJ4100

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
while 1:                                                # N이 0이 될때까지 반복해서
    N = int(input())                                    # N 도시의 수를 input 받는다
    if N == 0:                                          # N이 0이라면
        quit()                                          # 종료한다
    road = [[] for _ in range(N)]                       # 케이블의 정보를 저장하기 위한 리스트를 생성하고
    city = []                                           # 도시를 저장할 리스트를 생성한다
    for i in range(N):                                  # 도시의 수를 반복해서
        x, y = map(int, input().split())                # 도시의 좌표를 input 받고
        for j in range(i):                              # city에 저장된 도시의 수를 반복해서
            x1, y1 = city[j]                            # 저장된 도시의 좌표를 x1, y1에 저장한다
            cost = ((x-x1)**2 + (y-y1)**2)**(1/2)       # 두 도시 사이의 케이블의 길이를 cost에 저장하고
            road[i].append([cost, j])                   # i에 [케이블의 거리, j도시를 append
            road[j].append([cost, i])                   # j에 [케이블의 거리, i도시를 append
        city.append([x, y])                             # city에 input 받은 도시의 정보 [x,y]를 append 한다

    ans = 0                                             # 최소 거리를 저장할 변수를 생성하고
    cnt = 0                                             # 방문한 도시의 수를 저장할 변수를 생성한다
    visited = [0] * N                                   # 방문표시를 할 리스트를 생성하고
    tmp = [[0, 0]]                                      # 시작점을 넣은 tmp 리스트를 생성한다
    while cnt < N:                                      # cnt가 N이 되어 모든 도시를 방문할 때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # 케이블의 길이와 연결 도시를 heappop한 후
        if visited[node] == 0:                          # 연결 도시가 방문 전이라면
            visited[node] = 1                           # 방문표시를 하고
            ans += cost                                 # 연결 케이블의 길이를 ans에 더한 후
            cnt += 1                                    # 방문한 도시의 수를 1 더한다
            for r in road[node]:                        # 연결 도시와 연결된 케이블을 반복해서
                if visited[r[1]] == 0:                  # 케이블의 도착지가 방문 전이라면
                    heapq.heappush(tmp, r)              # tmp에 케이블과 도착지를 heappush한다
    print("{:.2f}".format(ans))                         # 최소 거리를 소수 2번째짜리까지 구해서 출력한다