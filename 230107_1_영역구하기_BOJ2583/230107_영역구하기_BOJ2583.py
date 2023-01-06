# 영역구하기_BOJ2583

# input.txt 열기
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(20000)

def color(x, y):
    global tmp                                      # tmp를 글로벌로 불러와서
    for i in range(4):                              # 상우하좌 4방향의 델타탐색을 반복하고
        if 0 <= x+dx[i] < M and 0<= y+dy[i] <N:     # 이동한 좌표가 행렬 내에 있을 때
            if visited[x+dx[i]][y+dy[i]] == 0:      # 이동한 좌표가 0이라면
                visited[x+dx[i]][y+dy[i]] = 2       # 2로 바꾸고
                tmp += 1                            # 분리된 영역의 넓이를 1증가시키고
                color(x+dx[i], y+dy[i])             # 이동한 좌표로 color함수를 통해 DFS 탐색한다

# input 받기
M, N, T = map(int, input().split())                 # M 행의길이 / N 열의길이 / T 직사각형의 수
visited = [[0]*N for _ in range(M)]                 # 요소가 모두 0인 M*N 행렬을 만들고
for t in range(T):                                  # 직사각형의 수만큼 반복해서
    A = list(map(int, input().split()))             # 직사각형의 대각선의 꼭지점을 input 받는다
    for i in range(A[1], A[3]):                     # 직사각형의 행을 반복하고
        for j in range(A[0], A[2]):                 # 직사각형의 열을 반복해서
            visited[i][j] = 1                       # 행렬위에 직사각형이 차지하는 영역의 요소를 1로 바꾼다

dx = [-1, 0, 1, 0]                                  # 행을 델타탐색하기 위한 리스트 (상우하좌)
dy = [0, 1, 0, -1]                                  # 열을 델타탐색하기 위한 리스트 (상우하좌)

cnt = 0                                             # 분리된 영역의 개수를 셀 변수를 생성하고
ans = []                                            # 분리된 영역의 넓이를 저장할 리스트를 생성한다
for i in range(M):                                  # 행을 반복하고
    for j in range(N):                              # 열을 반복해서
        if visited[i][j] == 0:                      # 해당 좌표의 요소의 값이 0이라면
            tmp = 0                                 # 분리된 영역의 넓이를 저장할 변수를 생성하고
            visited[i][j] = 2                       # 해당 좌표를 2로 변경하여 방문표시를 해준다
            tmp += 1                                # 분리된 영역의 넓이를 1증가시키고
            cnt += 1                                # 분리된 영역의 개수를 1증가시킨다
            color(i, j)                             # 해당 좌표로 color함수를 통해 DFS 탐색한 후
            ans.append(tmp)                         # 탐색을 마치면 분리된 영역의 넓이를 ans에 append

print(cnt)                                          # 분리된 영역의 개수를 출력하고
ans.sort()                                          # 오름차순으로 정렬한 후
print(*ans)                                         # 분리된 영역의 넓이를 출력한다다


