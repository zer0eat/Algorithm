# 해킹_BOJ10282

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반보갷서
    N, D, C = map(int, input().split())         # N 컴퓨터의수 / D 연결된 컴퓨터의 경로 / C 바이러스 걸린 컴퓨터
    road = [[] for _ in range(N)]               # 연결된 컴퓨터 경로를 저장할 리스트 생성
    for _ in range(D):                          # 연결된 컴퓨터 경로를 반복해서
        a, b, s = map(int, input().split())     # a, b 연결된 컴퓨터 s 연결 시간을 input 받는다
        road[b-1].append([s, a-1])              # b-1 인덱스에 [연결시간, 연결된 컴퓨터]를 append

    def dijkstra(start):
        distance = [1e9]*N                      # 각 컴퓨터까지의 시간을 저장할 리스트 생성
        distance[start] = 0                     # 시작점을 비용을 0으로 저장
        tmp = [[0, start]]                      # 시작점을 넣은채로 tmp 리스트 생성
        while tmp:                              # tmp가 빌때까지 반복해서
            cost, node = heapq.heappop(tmp)     # 시간과 다음 컴퓨터 정보를 heappop해서 꺼낸다
            if cost > distance[node]:           # 저장된 다음 컴퓨터까지 시간보다 cost가 더 크다면 최소시간이 아니므로
                continue                        # continue로 넘어간다
            for r in road[node]:                # 연결된 컴퓨터와 연결된 네트워크를 반복해서
                cost2 = cost + r[0]             # 현재 시간과 연결된 컴퓨터 시간을 더한 값을 cost2로 저장하고
                if distance[r[1]] > cost2:      # cost2가 연결된 컴퓨터까지 저장된 시간보다 작을 경우
                    distance[r[1]] = cost2      # cost2로 갱신하여 저장하고
                    heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [갱신된 시간, 도착컴퓨터]을 heapppush 한다
        return distance                         # while문이 종료되면 distance 리스트를 return 한다

    result = dijkstra(C-1)                      # 다익스트라 알고리즘으로 감염원으로 부터 감염된 시간을 계산
    ans = 0                                     # 감염된 컴퓨터의 수를 저장할 변수 생성
    maxV = 0                                    # 가장 오래 걸린 시간을 저장할 변수 생성
    for r in result:                            # 컴퓨터의 감염 목록을 반복해서
        if r != 1e9:                            # 감염시간이 측정된 컴퓨터라면
            ans += 1                            # 감염대수를 1 추가하고
            if maxV < r:                        # 감염시간이 maxV보다 크다면
                maxV = r                        # maxV를 갱신한다
    print(ans, maxV)                            # 감염된 컴퓨터의 수와 가장 오래걸린 시간을 출력한다