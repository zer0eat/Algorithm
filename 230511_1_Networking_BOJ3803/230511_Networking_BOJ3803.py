# Networking_BOJ3803

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
while 1:                                        
    A = list(map(int, input().split()))         # 지점의 수와 연결 케이블의 수를 list로 input 받는다
    if A[0] == 0:                               # 지점의 수가 0이라면
        quit()                                  # 종료한다
    road = [[] for _ in range(A[0])]            # 케이블의 정보를 저장할 리스트를 생성하고
    for _ in range(A[1]):                       # 케이블의 수 만큼 반복해서
        a, b, c = map (int, input().split())    # a, b 지점의 정보와 c 케이블의 길이를 input 받는다
        road[a-1].append([c, b-1])              # a 에서 이동할 수 있는 지점을 [케이블 길이, 연결 지점 정보] 형태로 append
        road[b-1].append([c, a-1])              # b 에서 이동할 수 있는 지점을 [케이블 길이, 연결 지점 정보] 형태로 append
    input()                                     # input 데이터 중 테스트 케이스를 나누기 위한 빈 공백을 input 받는다
    
    ans = 0                                     # 최소 길이를 저장할 변수 생성
    visited = [0] * A[0]                        # 방문 기록을 저장할 리스트를 생성한다
    tmp = [[0, 0]]                              # 시작점을 넣은 tmp 리스트를 생성하고
    while tmp:                                  # tmp가 빌 때까지 반복해서
        cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 케이블 길이와 연결 지점 정보를 저장한다
        if visited[node] == 0:                  # 연결 지점이 방문 전이라면
            visited[node] = 1                   # 방문표시를 하고
            ans += cost                         # 케이블 길이를 ans에 더해준다
            for r in road[node]:                # 연결 지점에 연결된 케이블을 반복해서
                if visited[r[1]] == 0:          # 케이블의 도착지가 방문 전이라면
                    heapq.heappush(tmp, r)      # tmp에 heappush 한다
    print(ans)                                  # 케이블의 최소 길이를 출력한다