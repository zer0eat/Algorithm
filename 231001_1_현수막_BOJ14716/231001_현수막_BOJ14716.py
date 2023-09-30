# 현수막_BOJ14716

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
M, N = map(int, input().split())                    # M 현수막의 행의 길이 / N 현수막의 열의 길이를 input 받고
banner = [list(map(int, input().split())) for _ in range(M)]                # 현수막의 정보를 행렬로 input 받고
visited = [[0]*N for _ in range(M)]                 # 방문표시를 할 행렬을 생성한다
d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]  # 8방향으로 이동할 리스트를 생성하고
ans = 0                                             # 정답을 저장할 변수를 생성해서
for i in range(M):                                  # 행을 반복하고
    for j in range(N):                              # 열을 반복해서
        if visited[i][j] == 0 and banner[i][j]:     # 해당 원소가 방문 전이고 글자인 부분이라면
            ans += 1                                # 글자의 수를 1 추가하고
            lst = deque([[i, j]])                   # deque에 시작점을 넣어 생성하고
            visited[i][j] = 1                       # 시작점을 방문 표시한다
            while lst:                              # lst가 빌때까지 반복해서
                r, c = lst.popleft()                # 행과 열을 popleft한다
                for t in range(8):                  # 8방향을 반복해서
                    x = r + d[t][0]                 # x에 이동한 행을 저장하고
                    y = c + d[t][1]                 # y에 이동한 열을 저장해서
                    if 0<=x<M and 0<=y<N:           # 이동한 곳이 현수막 내에 있으면서
                        if visited[x][y] == 0 and banner[x][y]:             # 방문 전이고 글자인 부분이라면
                            visited[x][y] = 1       # 방문 표시를 하고
                            lst.append([x, y])      # lst에 append 한다
print(ans)                                          # 현수막에서 글자의 개수가 몇 개인지 출력한다