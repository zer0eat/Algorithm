# 나만안되는연애_BOJ14621

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 학교의 수 / M 학교를 연결하는 도로의 수 
school = list(input().split())              # 남자대학교인지 여자대학교인지 리스트로 input 받고
line = [[] for _ in range(N)]               # 학교를 연결하는 도로와 경로의 길이 정보를 저장할 리스트 생성

for i in range(M):                          # 연결하는 도로의 수를 반복해서
    a, b, c = map(int, input().split())     # a 학교 / b 학교 / c 두 학교의 길이를 input 받고 
    if school[a-1] != school[b-1]:          # 리스트의 인덱스는 0부터 시작하므로 모든 학교의 인덱스를 한 칸 씩 당긴 후 a 학교와 b 학교가 남 녀 대학인 경우에만
        line[a-1].append([c, b-1])          # a 학교 인덱스의 위치에 [비용, b학교]를 append
        line[b-1].append([c, a-1])          # b 학교 인덱스의 위치에 [비용, a학교]를 append

tmp = [[0, 0]]                              # tmp 리스트 안에 시작점 [0, 1]을 넣고 생성해서
visited = [0]*N                             # 방문 표시 할 리스트를 생성한다
ans = 0                                     # 총 비용을 계산할 변수를 생성하고
while tmp:                                  # tmp가 빌 때까지 반복해서
    A = heapq.heappop(tmp)                  # tmp에서 heappop해서 A에 저장한 후
    if visited[A[1]] == 0:                  # 연결할 학교가 아직 방문 전이라면
        visited[A[1]] = 1                   # 연결할 학교에 방문표시를 한 후
        ans += A[0]                         # 연결비용을 ans에 더한다
        for r in line[A[1]]:                # 연결할 학교와 연결된 길을 반복해서
            if visited[r[1]] == 0:          # 연결할 학교와 연결된 학교 중 방문 전인 학교가 있다면
                heapq.heappush(tmp, r)      # tmp에 heappush 한다

if sum(visited) == N:                       # visited의 합이 N이 되어 모든 학교가 이어졌다면
    print(ans)                              # ans를 출력하고
else:                                       # 이어지지 않았다면
    print(-1)                               # -1을 출력한다