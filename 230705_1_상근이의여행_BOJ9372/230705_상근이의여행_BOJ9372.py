# 상근이의여행_BOJ9372

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):                              # 테스트 케이스를 반복해서
    N, M = map(int, input().split())            # N 방문 나라 / M 비행기 수
    flight = [[] for _ in range(N)]             # 비행기 정보를 저장할 리스트 생성
    for m in range(M):                          # 비행기 수를 반복해서
        a, b = map(int, input().split())        # 비행기가 다니는 두 나라를 input 받고
        flight[a-1].append([1, b-1])            # a에서 출발했을 때 [비행기 탑승 수, 도착나라]를 append
        flight[b-1].append([1, a-1])            # b에서 출발했을 때 [비행기 탑승 수, 도착나라]를 append
    nation = [0] * N                            # 방문한 나라를 기록할 리스트 생성
    tmp = [[0, 0]]                              # 시작점을 넣고 tmp 리스트를 생성한다
    ans = 0                                     # 정답을 저장할 변수 생성
    while tmp:                                  # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)         # tmp에서 비용과 도착나라를 heappop한 후
        if nation[node] == 0:                   # 도착나라가 방문 전이라면
            nation[node] = 1                    # 도착나라를 방문표시하고
            ans += 1                            # 탑승 비행기 수를 1 추가한다
            for r in flight[node]:              # 도착나라와 연결된 비행편을 반복해서
                if nation[r[1]] == 0:           # 비행편의 도착지가 방문 전이라면
                    heapq.heappush(tmp, r)      # tmp에 해당 비행편을 heappush
    print(ans-1)                                # 모든 국가를 여행하기 위해 탑승해야하는 비행기의 수를 출력한다