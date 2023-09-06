# 무기공학_BOJ18430

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def dfs(i ,j, cnt):
    global ans, N, M                                                # ans, N, M을 global 변수로 불러오고
    if j == M:                                                      # 행의 끝에 도달하면
        i += 1                                                      # 행을 다음 칸으로 이동하고
        j = 0                                                       # 열을 맨 앞칸으로 이동한다
    if i == N:                                                      # 마지막 행에 도달했다면
        ans = max(ans, cnt)                                         # ans에 ans와 cnt 중 더 큰 수로 저장하고
        return                                                      # return 한다
    if visited[i][j] == 0:                                          # i, j가 방문 전이라면
        for k in range(4):                                          # shape의 4방향을 반복해서
            a, b, c, d = shape[k]                                   # i,j를 중심으로 부메랑을 만들 수 있는 양 날개 위치를 a,b,c,d에 저장하고
            x, y, xx, yy = i+a, j+b, i+c, j+d                       # 한 쪽 날개를 x, y에 i+a, i+b로 저장하고 다른 날개를  xx, yy에 i+c, i+d로 저장한다
            if 0 <= x < N and 0 <= xx < N and 0<=y<M and 0<=yy<M and visited[x][y] == 0 and visited[x][y] == 0 and visited[xx][yy] == 0:   # x, y, xx, yy가 행렬 내에 있고 방문 전일 때
                visited[x][y] = 1                                   # x,y를 방문 표시하고
                visited[xx][yy] = 1                                 # xx, yy를 방문 표시하고
                visited[i][j] = 1                                   # i, j를 방문 표시하고
                dfs(i, j+1, cnt+wood[i][j]*2 + wood[x][y] + wood[xx][yy])       # i, j에서 한칸 옆으로 이동하고 강도의 합 넣고 dfs 탐색한 후
                visited[x][y] = 0                                   # x,y를 방문 표시를 해제한다
                visited[xx][yy] = 0                                 # xx,yy를 방문 표시를 해제한다
                visited[i][j] = 0                                   # i,j를 방문 표시를 해제한다
    dfs(i, j+1, cnt)                                                # i, j에서 한칸 옆으로 이동하고 강도의 합 넣고 dfs 탐색힌다

N, M = map(int, input().split())                                    # N 나무재료의 행 / M 나무재료의 열을 input 받고
wood = [list(map(int, input().split())) for _ in range(N)]          # 나무재료의 강도를 저장한 행렬을 input 받는다
shape = [[0,-1,1,0], [-1,0,0,-1], [-1,0,0,1], [0,1,1,0]]            # 부메랑의 중심으로 만들 수 있는 4가지 방향 리스트를 생성한다
visited = [[0]*M for _ in range(N)]                                 # 부메랑 재료로 사용한 위치를 표시할 행렬을 생성하고
ans = 0                                                             # 부메랑 강도의 합을 저장할 변수를 생성한다
dfs(0, 0, 0)                                                        # 부메랑을 만드는 dfs탐색을 한다
print(ans)                                                          # 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력한다