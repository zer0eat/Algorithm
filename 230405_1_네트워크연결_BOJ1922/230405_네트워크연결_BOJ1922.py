# 네트워크연결_BOJ1922

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                            # 컴퓨터의 수
M = int(input())                            # 연결할 수 있는 경우의 수

computer = [[] for _ in range(N+1)]         # computer의 연결비용을 저장할 리스트를 생성하고

for i in range(M):                          # 연결할 수 있는 경우의 수를 반복해서
    a, b, c = map(int, input().split())     # 컴퓨터 a, 컴퓨터 b, 비용 c를
    computer[a].append([c, b])              # 컴퓨터의 a 인덱스에 [비용, 연결할 컴퓨터]를 append 
    computer[b].append([c, a])              # 컴퓨터의 b 인덱스에 [비용, 연결할 컴퓨터]를 append

ans = 0                                     # 모든 컴퓨터의 연결비용을 저장할 변수를 생성하고
visited = [0]*(N+1)                         # 컴퓨터의 방문표시를 할 리스트를 생성한다
tmp = [[0, 1]]                              # tmp에 시작점을 넣은고 리스트를 생성하고
while tmp:                                  # tmp가 빌때까지 while을 반복한다
    cost, node = heapq.heappop(tmp)         # tmp에서 heapqpop하여 cost에 비용을 저장하고 node에 연결할 컴퓨터를 저장한다
    if visited[node] == 0:                  # 연결할 컴퓨터가 방문 전이라면
        visited[node] = 1                   # 방문표시를 한 후
        ans += cost                         # 연결비용을 ans에 더한다
        for r in computer[node]:            # 연결할 컴퓨터와 연결된 컴퓨터 리스트를 반복해서
            if visited[r[1]] == 0:          # node 컴퓨터와 연결된 컴퓨터가 아직 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush한다
print(ans)                                  # while문이 종료 되었다면 ans를 출력한다