# 도로_BOJ9344

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input().strip())                                # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복해서
    N, K, x, y = map(int, input().split())              # N 도시 / K 도로 / x, y 연결되어있어야하는 도시
    road = [[] for _ in range(N)]                       # 길을 저장할 리스트를 생성하고
    for _ in range(K):                                  # 길의 수를 반복해서
        a, b, c = list(map(int, input().split()))       # a, b 도시와 c 비용을 input 받는다
        road[a-1].append([c, b-1, a-1])                 # road의 a-1 인덱스에 [비용, 연결할 도시, 기준도시] append
        road[b-1].append([c, a-1, b-1])                 # road의 b-1 인덱스에 [비용, 연결할 도시, 기준도시] append

    tmp = [[0, 0, 0]]                                   # tmp에 시작점을 넣고 시작해서
    flag = "NO"                                         # flag를 NO로 생성한다
    visited = [0] * N                                   # 방문 표시를할 리스트를 생성하고 
    while tmp:                                          # tmp가 빌때까지 반복해서
        A = heapq.heappop(tmp)                          # A에 tmp에서 heappop한 것을 저장한 후
        if visited[A[1]] == 0:                          # 연결할 도시가 방문 전이라면
            aaa = [A[1], A[2]]                          # 연결할 도시와 이어진 도시를 aaa 리스트에 저장한다
            aaa.sort()                                  # aaa리스트를 오름차순으로 정렬한 후
            if aaa == [x-1, y-1]:                       # aaa와 연결할 두 도시 [x-1, y-1]의 리스트가 같다면 
                flag = "YES"                            # flag를 YES로 바꾼다
            visited[A[1]] = 1                           # 연결할 도시를 방문표시한 후
            for r in road[A[1]]:                        # 연결할 도시와 연결된 도시를반복해서
                if visited[r[1]] == 0:                  # 연결된 도시가 방문 전이라면
                    heapq.heappush(tmp, r)              # tmp에 heappush 한다
    print(flag)                                         # flag를 출력하여 x-y 도로망을 포함한 가장 짧은 도로를 건설할 수 있는지 출력한다