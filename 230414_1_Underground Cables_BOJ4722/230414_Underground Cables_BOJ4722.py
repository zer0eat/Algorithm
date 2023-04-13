# Underground Cables_BOJ4722

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
import math

# input 받기
while 1:                                        # N이 0이 나올 때까지 반복해서
    N = int(input().strip())                    # N 도시의 수
    if N == 0:                                  # N이 0이 나오면
        quit()                                  # 종료한다
    road = [[] for _ in range(N)]               # 도시의 연결정보를 저장할 리스트 생성하고
    cable = []                                  # 케이블의 정보를 저장할 리스트를 생성한다
    for i in range(N):                          # 도시의 수를 반복해서
        A = list(map(int, input().split()))     # 도시의 좌표를 리스트 형태로 A에 저장한다
        for j in range(len(cable)):             # 케이블 리스트를 반복해서
            distance = math.sqrt((A[0]-cable[j][0])**2 + (A[1]-cable[j][1])**2) # 두 도시 사이의 거리를 distance에 저장하고
            road[i].append([distance, j])       # i인덱스에 [i와 j의 거리, j도시]를 append
            road[j].append([distance, i])       # j인덱스에 [i와 j의 거리, i도시]를 append
        cable.append(A)                         # cable에 A를 append

    ans = 0                                     # 정답을 저장할 변수를 생성하고
    visited = [0] * N                           # 방문표시를 할 리스트를 생성한다
    tmp = [[0, 0]]                              # 시작점을 넣은 tmp 리스트를 생성하고
    cnt = 0                                     # 연결도시의 수를 저장할 변수를 생성한다
    while tmp:                                  # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 cost와 node를 저장한다
        if visited[node] == 0:                  # node 도시가 방문 전이라면
            ans += cost                         # ans에 연결비용을 추가하고
            visited[node] = 1                   # node 도시를 방문표시한다
            cnt += 1                            # 연결도시의 수를 1 추가하고
            if cnt == N:                        # 연결도시의 수가 N이라면
                break                           # while문을 break 한다
            for r in road[node]:                # node 도시와 연결된 도시를 반복해서
                if visited[r[1]] == 0:          # 연결된 도시가 방문 전이라면
                    heapq.heappush(tmp, r)      # tmp에 heappush한다
    print("{:.2f}".format(ans))                 # 연결비용을 소수 2번째자리까지 출력한다