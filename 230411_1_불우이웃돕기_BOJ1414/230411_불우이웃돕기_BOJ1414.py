# 불우이웃돕기_BOJ1414

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                # 컴퓨터의 개수
com = [[] for _ in range(N)]                    # 연결할 컴퓨터의 랜선의 길이를 저장
total = 0                                       # 전체 랜선의 길이를 저장할 변수를 생성
for i in range(N):                              # 컴퓨터의 개수를 반복해서
    A = list(input().strip())                   # 랜선의 길이를 A에 저장한다
    for j in range(N):                          # 컴퓨터의 개수를 반복해서
        if A[j] != '0':                         # 랜선의 길이가 0이 아니라면
            tmp = ord(A[j]) % 96                # tmp에 랜선의 길이를 저장한다
            if tmp > 26:                        # 랜선의 길이가 26보다 크다면
                tmp -= 38                       # tmp에서 38을 빼준다
                total += tmp                    # total에 tmp를 더하고
                if i != j:                      # i와 j가 다른 컴퓨터라 서로 연결해야한다면
                    com[i].append([tmp, j])     # i인덱스에 [랜선의 길이, 연결할 컴퓨터]를 append
                    com[j].append([tmp, i])     # j인덱스에 [랜선의 길이, 연결할 컴퓨터]를 append
            else:                               # 랜선의 길이가 26이하라면
                total += tmp                    # total에 tmp를 더하고
                if i != j:                      # i와 j가 다른 컴퓨터라 서로 연결해야한다면
                    com[i].append([tmp, j])     # i인덱스에 [랜선의 길이, 연결할 컴퓨터]를 append
                    com[j].append([tmp, i])     # j인덱스에 [랜선의 길이, 연결할 컴퓨터]를 append

tmp = [[0, 0]]                                  # tmp리스트에 [랜선의 길이, 시작점]을 넣고 생성한다
visited = [0] * N                               # 방문기록을 표시할 리스트 생성
ans = 0                                         # 최단길이를 저장할 변수생성
while tmp:                                      # tmp가 빌때까지 반복해서
    A = heapq.heappop(tmp)                      # tmp에서 heappop해서 A에 저장하고
    if visited[A[1]] == 0:                      # 연결할 컴퓨터가 방문 전이라면
        ans += A[0]                             # ans에 랜선의 길이를 더하고
        visited[A[1]] = 1                       # 연결할 컴퓨터를 방문표시해준다
        for r in com[A[1]]:                     # 연결할 컴퓨터와 연결된 컴퓨터를 반복해서
            if visited[r[1]] == 0:              # 연결할 컴퓨터와 이어져 있는 컴퓨터가 방문 전이라면
                heapq.heappush(tmp, r)          # tmp에 heappush한다
if sum(visited) == N:                           # visited의 합이 N이라 모든 컴퓨터가 연결되었다면
    print(total - ans)                          # 전체 랜선의 길이에서 최소랜선의 길이를 뺀 값을 출력하고
else:                                           # visited의 합이 N이 아니라 모든 컴퓨터가 연결되지 않았다면
    print(-1)                                   # -1을 출력한다