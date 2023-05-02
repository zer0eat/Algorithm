# 비밀모임_BOJ13424

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input())                                            # 테스트케이스
for t in range(T):                                          # 테스트 케이스를 반복해서
    N, M = map(int, input().split())                        # N 비밀의 방 개수 / M 비밀통로의 수
    road = [[] for _ in range(N)]                           # 비밀 통로를 저장할 리스트 생성
    for _ in range(M):                                      # 비밀 통로의 수를 반복해서
        a, b, c = map(int, input().split())                 # a,b 비밀의 방 c 비용을 input 받는다
        road[a-1].append([c, b-1])                          # a 방에서 이동할 수 있는 곳을 [비용, 연결 방]을 append
        road[b-1].append([c, a-1])                          # b 방에서 이동할 수 있는 곳을 [비용, 연결 방]을 append

    def dijksatra(start):
        distance = [1e9] * N                                # 방까지 이동 시간을 저장할 리스트 생성
        distance[start] = 0                                 # start 방까지 이동 비용을 0으로 저장
        tmp = [[0, start]]                                  # tmp에 [시작비용, 시작점]을 넣고 리스트 생성
        while tmp:                                          # tmp가 빌때까지 반복해서
            cost, node = heapq.heappop(tmp)                 # tmp에서 비용과 연결 비밀의방 정보를 heappop한다
            if cost > distance[node]:                       # cost가 현재 저장된 비밀의 방 이동비용보다 크다면
                continue                                    # continue
            for r in road[node]:                            # 이동한 비밀의 방에서 연결된 통로를 반복해서
                cost2 = cost + r[0]                         # 현재까지 이동비용과 연결된 통로의 비용을 더한값을 cost2에 저장하고
                if cost2 < distance[r[1]]:                  # cost2가 현재 저장된 비용보다 작다면
                    distance[r[1]] = cost2                  # cost2를 저장비용으로 바꿔 저장하고
                    heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [이동비용, 비밀통로의 도착지]로 heappush
        return distance                                     # distance를 return한다
    
    K = int(input())                                        # 친구의 수
    friend = list(map(int, input().split()))                # 친구가 있는 방의 번호를 리스트로 input
    
    ans = [0]*N                                             # 각 방까지 이동 비용을 저장할 리스트를 생성하고
    for f in friend:                                        # 친구가 있는 방의 리스트를 반복해서
        result = dijksatra(f-1)                             # 친구 위치에서 각방까지 최소 이동비용을 구해 리스트로 저장하고
        for l in range(N):                                  # 리스트를 반복하며
            ans[l] += result[l]                             # 각방까지 이동비용을 ans 리스트에 더해준다

    answer = 0                                              # 최소 이동 비용의 방번호를 저장할 변수 생성
    tmp = 1e9                                               # 최소 이동 비용을 저장할 변수 생성
    for l in range(N):                                      # 친구의 수를 반복해서
        if tmp > ans[l]:                                    # l번 방의 비용이 tmp보다 작다면
            tmp = ans[l]                                    # tmp에 최소 비용을 저장하고
            answer = l+1                                    # answer에 최소비용의 방번호를 저장한다
    print(answer)                                           # 최소비용으로 모일 수 있는 방 번호를 출력한다
