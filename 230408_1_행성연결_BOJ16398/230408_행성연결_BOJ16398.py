# 행성연결_BOJ16398

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                            # 행성의 수를 input 받고
star = [[] for _ in range(N)]               # 행성끼리 연결 비용을 저장할 리스트를 생성한다

for i in range(N):                          # 행성의 수를 반복하고
    A = list(map(int, input().split()))     # A에 i번 행성과 연결되는 비용을 리스트로 input 받고
    for j in range(i+1, N):                 # i번 인덱스 다음부터 반복해서
        star[i].append([A[j], j])           # i인덱스에 [비용, 연결할 행성]을 append
        star[j].append([A[j], i])           # j인덱스에 [비용, 연결할 행성]을 append

ans = 0                                     # 최소 비용을 저장할 변수 생성
visited = [0]*N                             # 방문표시를 할 리스트 생성
tmp = [[0, 0]]                              # [0, 시작점]을 넣은 리스트 생성
while tmp:                                  # tmp가 빌때까지 반복해서
    A = heapq.heappop(tmp)                  # A에 tmp에서 heappop해서 저장
    if visited[A[1]] == 0:                  # 연결될 노드가 방문 전이라면
        visited[A[1]] = 1                   # 연결표시를 하고
        ans += A[0]                         # 비용을 ans에 더한다
        for r in star[A[1]]:                # 연결될 노드와 연결할 수 있는 노드를 탐색하여
            if visited[r[1]] == 0:          # 연결할 수 있는 노드가 방문전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush 한다
print(ans)                                  # 최소비용을 출력한다