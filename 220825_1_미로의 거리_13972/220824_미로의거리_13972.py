# 미로의 거리_13972

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from pprint import pprint
# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스 만큼 반복
    N = int(input())                                            # N = 행렬의 길이
    miro = [list(map(int, input())) for _ in range(N)]          # miro = 길이가 N인 행렬

    # 시작점 찾기
    for i in range(N):                                          # 미로의 행의 길이 만큼 반복
        for j in range(N):                                      # 미로의 열의 길이 만큼 반복
            if miro[i][j] == 2:                                 # 시작점을 찾았다면
                a = i                                           # 행을 a에 저장
                b = j                                           # 열을 b에 저장

    # 도착점 찾기
    for i in range(N):                                          # 미로의 행의 길이 만큼 반복
        for j in range(N):                                      # 미로의 열의 길이 만큼 반복
            if miro[i][j] == 3:                                 # 시작점을 찾았다면
                Ea = i                                          # 행을 a에 저장
                Eb = j                                          # 열을 b에 저장

    # 미로 찾기
    q = []                                                      # q를 생성
    q.append((a, b))                                            # 시작점을 q에 append
    miro[a][b] = -1                                             # 시작점을 -1로 지정해 준 후
    dr = [-1, 0, 1, 0]                                          # 델타 탐색을 위한 row의 이동거리(상 우 하 좌)
    dc = [0, 1, 0, -1]                                          # 델타 탐색을 위한 col의 이동거리(상 우 하 좌)

    while q:                                                    # q가 빌 때까지 반복할 때
        a, b = q.pop(0)                                         # q에서 가장 오래된 요소를 pop
        for i in range(4):                                      # 델타탐색을 할 때
            if a+dr[i] != -1 and a+dr[i] != N and b + dc[i] != -1 and b + dc[i] != N: # 행렬을 벗어나지 않는 경우
                if miro[a+dr[i]][b+dc[i]] == 3:                 # 도착지점을 만나면
                    miro[a + dr[i]][b + dc[i]] = miro[a][b] - 1     # 도착지점을 그 전 칸보다 -1한 값으로 저장
                elif miro[a+dr[i]][b+dc[i]] == 0:               # 갈 수 있는 길일 때
                    miro[a + dr[i]][b + dc[i]] = miro[a][b] - 1     # 그 전 칸보다 -1한 값으로 저장
                    q.append((a+dr[i], b+dc[i]))                # 큐에 갈 수 있는 길을 append
    pprint(miro)
    if miro[Ea][Eb] < 0:                                        # 도착지점의 값이 음수이면 도착한 것이므로
        print(f'#{t+1}', abs(miro[Ea][Eb]+2))                   # 도착지점과 출발사이의 0의 개수인 miro[Ea][Eb]+2를 출력
    else:                                                       # 음수가 아니라면 도착하지 못했으므로
        print(f'#{t + 1}', 0)                                   # 0을 출력한다