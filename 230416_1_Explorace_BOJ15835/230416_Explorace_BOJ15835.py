# Explorace_BOJ15835

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
import math

# input 받기
T = int(input().strip())                        # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    N, M = map(int, input().split())            # N 체크포인트의 수 / M 연결의 수
    road = [[] for _ in range(N)]               # 연결 정보를 저장할 리스트 생성
    for _ in range(M):                          # 연결의 수를 반복해서
        a, b, c = map(int, input().split())     # 연결할 체크포인트 a,b 비용 c를 input 받는다
        road[a-1].append([c, b-1])              # a인덱스에 [비용, 연결 체크포인트]를 append
        road[b-1].append([c, a-1])              # b인덱스에 [비용, 연결 체크포인트]를 append

    tmp = [[0, 0]]                              # 시작점을 넣은 tmp 리스트를 생성하고
    ans = 0                                     # 최소 비용을 저장할 변수를 생성한다
    visited = [0]*N                             # 방문 표시를할 리스트를 생성하고
    while tmp:                                  # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)         # 연결비용과 연결 포인트를 heappop해서
        if visited[node] == 0:                  # 연결 포인트가 방문 전이라면
            visited[node] = 1                   # 방문 표시 후
            ans += cost                         # 연결비용을 ans에 더한다
            for r in road[node]:                # 연결 포인트와 연결된 장소를 반복하여
                if visited[r[1]] == 0:          # 해당 장소도 방문 전이라면
                    heapq.heappush(tmp, r)      # tmp에 heappush한다
    print(f'Case #{t+1}: {ans} meters')         # 테스트 케이스와 최소비용을 출력한다