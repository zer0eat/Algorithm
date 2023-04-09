# 정복자_BOJ14950

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, t = map(int, input().split())         # N 도시의 개수 / M 도로의 개수 / t 정복시 증가하는 비용
city = [[] for _ in range(N)]               # 도로를 연결할 때 드는 비용과 연결될 도시를 저장할 리스트 생성
for _ in range(M):                          # 도로의 개수를 반복해서
    a, b, c = map(int, input().split())     # a도시 b도시 c연결비용을 input 받는다
    city[a-1].append([c, b-1])              # a-1인덱스에 [연결비용, 연결할도시]를 append
    city[b-1].append([c, a-1])              # b-1인덱스에 [연결비용, 연결할도시]를 append

ans = 0                                     # 정답을 저장할 변수 생성
plus = 0                                    # 정복시 증가하는 비용을 저장할 변수 생성
visited = [0] * N                           # 방문 기록을 저장할 리스트생성
visited[0] = 1                              # 출발점을 방문표시하고
tmp = []                                    # 연결할 도시를 임시로 저장할 리스트를 생성한 후
for r in city[0]:                           # 출발점과 연결된 도로정보를 반복해서
    if visited[r[1]] == 0:                  # 방문전인 도시라면 
        heapq.heappush(tmp, r)              # tmp에 heappush한다
        
while tmp:                                  # tmp가 빌 때까지 반복해서
    cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 비용과 연결할 도시를 저장한다
    if visited[node] == 0:                  # 연결할 도시가 아직 방문 전이라면
        ans += (cost + plus)                # ans에 연결비용과 증가비용을 더하고
        plus += t                           # 증가비용에 t를 더해준 후
        visited[node] = 1                   # 연결할 도시를 방문표시해준다
        for r in city[node]:                # 연결할 도시와 연결된 도로를 반복해서
            if visited[r[1]] == 0:          # 연결할 도시와 연결되는 도시가 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush한다
print(ans)                                  # tmp가 비어 while문이 종료되면 총 비용을 출력한다