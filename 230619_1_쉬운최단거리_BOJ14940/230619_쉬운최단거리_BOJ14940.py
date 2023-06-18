# 쉬운최단거리_BOJ14940

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                                    # N 세로의 크기 / M 가로의 크기
jido = [list(map(int, input().split())) for _ in range(N)]          # 지도를 리스트로 input 받는다
visited = [[0] * M for _ in range(N)]                               # 방문기록을 저장할 리스트를 생성하고
dx = [-1, 0, 1, 0]                                                  # 델타 탐색으로 행의 위치를 이동할 리스트를 생성하고
dy = [0, 1, 0, -1]                                                  # 델타 탐색으로 열의 위치를 이동할 리스트를 생성한다

for i in range(N):                                                  # 행을 반복하고
    for j in range(M):                                              # 열을 반복해서
        if jido[i][j] == 2:                                         # 해당 위치가 2가 나왔다면
            tmp = [[0, i, j]]                                       # tmp를 [거리, 행의위치, 열의위치]를 넣고 리스트를 생성한다
            while tmp:                                              # tmp가 빌때까지 반복해서
                cost, n, m = heapq.heappop(tmp)                     # 거리, 행의위치, 열의위치를 heappop해서
                if visited[n][m] == 0 and jido[i][j] != 0:          # 방문 전이면서 갈 수 있는 위치인 경우에
                    visited[n][m] = cost                            # 해당 지역을 거리로 표시하고
                    for t in range(4):                              # 델타탐색을 진행한다
                        if 0 <= n + dx[t] < N and 0 <= m + dy[t] < M and jido[n + dx[t]][m + dy[t]] != 0 and visited[n + dx[t]][m + dy[t]] == 0:   # 지도 내의 위치면서 막다른 길이 아니면서 방문 전이라면
                            heapq.heappush(tmp, [cost + 1, n + dx[t],  m + dy[t]])  # tmp에 거리와 해당위치를 heappush
            else:                                                   # while문을 마쳤다면
                visited[i][j] = 0                                   # 시작점의 거리를 0으로 표시하고
                for i in range(N):                                  # 행을 반복하고
                    for j in range(M):                              # 열을 반복해서
                        if jido[i][j] == 1 and visited[i][j] == 0:  # 지도에 1인데 방문을 하지 못한 경우는
                            visited[i][j] = -1                      # -1로 표시하고
                for v in visited:                                   # 방문 기록을 반복해서
                    print(*v)                                       # 한 행씩 출력한 후
                quit()                                              # 종료한다