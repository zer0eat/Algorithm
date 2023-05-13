# 전기가부족해_BOJ10423

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, K = map(int, input().split())         # N 도시의 수 / M 케이블의 수 / K 발전소의 수
tmp = []                                    # 최소 비용 연결을 위해 케이블 정보를 저장할 리스트 생성
plant = map(int, input().split())           # 발전소를 세울 곳을 리스트로 input 받고
plant2 = dict()                             # 발전소 정보를 저장할 딕셔너리 생성
for p in plant:                             # 발전소를 반복해서
    plant2[p-1] = 1                         # 발전소 정보를 딕셔너리에 저장하고
    heapq.heappush(tmp, [0, p-1])           # tmp에 [연결비용 0, 건설 도시]를 heappush

road = [[] for _ in range(N)]               # 케이블 비용과 연결 도시를 저장할 리스트 생성
for _ in range(M):                          # 케이블의 수를 반복해서
    a, b, c = map(int, input().split())     # a,b 연결 도시와 c 연결 비용을 input 받고
    road[a-1].append([c, b-1])              # a 도시에서 연결된 케이블 정보 [연결비용, 연결도시]를 append
    road[b-1].append([c, a-1])              # b 도시에서 연결된 케이블 정보 [연결비용, 연결도시]를 append

ans = 0                                     # 최소 비용을 저장할 변수 생성
visited = [0] * N                           # 도시의 방문표시를 기록할 리스트생성
while tmp:                                  # tmp가 빌때까지 반복해서
    cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 비용과 연결 도시정보를 받고
    if visited[node] == 0:                  # 해당 도시가 방문 전이라면
        visited[node] = 1                   # 방문 표시를 해준 후
        ans += cost                         # 비용을 정답에 추가한다
        for r in road[node]:                # 도시와 연결된 케이블을 반복해서
            if visited[r[1]] == 0 and plant2.get(r[1]) == None: # 케이블의 도착지가 방문 전이고 발전소가 세워지지 않은 곳이라면
                heapq.heappush(tmp, r)      # tmp에 heappush 한다
print(ans)                                  # 도시의 전기를 공급하기 위한 최소 연결 비용을 출력한다