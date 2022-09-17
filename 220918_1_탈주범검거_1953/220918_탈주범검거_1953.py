# 탈주범검거_1953

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for p in range(T):                                                  # 테스트 케이스를 반복할 때
    N, M, r, c, t = map(int, input().split())                       # N = 세로의 길이 /  M = 가로의 길이 / r = 시작점의 행 / c = 시작점의 열 / t = 시간

    manhol = [list(map(int, input().split())) for _ in range(N)]    # 맨홀의 지도를 행렬로 받음

    q = []                                                          # 시작점 부터 순서대로 지나갈 수 있는 통로를 저장할 리스트
    ans = []                                                        # 도둑이 지나간 경로를 저장할 리스트

    q.append([r, c, 1])                                             # q에 [시작점r, 시작점c, 시간]을 넣고 시작

    while q:                                                        # q가 빌때까지 반복할 때
        i, j, T = q.pop(0)                                          # q에서 맨 앞에 있는 좌표를 꺼내 / 행의 위치를 i / 열의 위치를 j / 걸린시간을 T라고 저장한다

        for w in ans:                                               # 지나간 경로를 확인해서
            if [w[0], w[1]] == [i, j]:                              # 지나간 적이 있는 경로라면 반복을 멈추고 그 길은 다시 추가하지 않는다
                break
        else:                                                       # 지나간 적이 한 번도 없는 통로라면
            ans.append([i, j, T])                                   # 지나간 경로에 [행의위치, 열의위치, 걸린시간+1]을 저장한다

        if manhol[i][j] == 1:                                       # 현재 좌표의 경로가 1이라면 상우하좌를 지나 갈 수 있으므로
            if 0 <= i - 1 < N and manhol[i - 1][j] in [1,2,5,6]:    # 올라 갈 때 행렬 범위 내에서 다음 통로가 아래쪽으로 뚫려 있어 지나갈 수 있다면
                q.append([i-1, j, T + 1])  # 상                     # q에 추가해서 다음 경로로 이동한다
            if 0 <= j + 1 < M and manhol[i][j + 1] in [1,3,6,7]:    # 오른쪽으로 갈 때 행렬 범위 내에서 다음 통로가 왼쪽으로 뚫려 있어 지나갈 수 있다면
                q.append([i, j+1, T + 1])  # 우                     # q에 추가해서 다음 경로로 이동한다
            if 0 <= i + 1 < N and manhol[i + 1][j] in [1,2,4,7]:    # 내려 갈 때 행렬 범위 내에서 다음 통로가 위쪽으로 뚫려 있어 지나갈 수 있다면
                q.append([i+1, j, T + 1])  # 하                     # q에 추가해서 다음 경로로 이동한다
            if 0 <= j - 1 < M and manhol[i][j - 1] in [1,3,4,5]:    # 왼쪽으로 갈 때 행렬 범위 내에서 다음 통로가 오른쪽으로 뚫려 있어 지나갈 수 있다면
                q.append([i, j-1, T + 1])  # 좌                     # q에 추가해서 다음 경로로 이동한다
            manhol[i][j] = 0                                        # 지나갈 수 있는 길을 모두 찾았다면 다시 돌아와 탐색을 반복하지 않도록 지도에서 통로를 삭제한다
        elif manhol[i][j] == 2:                                     # 현재 좌표의 경로가 2라면 상하를 지나 갈 수 있으므로
            if 0 <= i - 1 < N and manhol[i - 1][j] in [1,2,5,6]:    # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i - 1, j, T + 1])  # 상
            if 0 <= i + 1 < N and manhol[i + 1][j] in [1,2,4,7]:
                q.append([i + 1, j, T + 1])  # 하
            manhol[i][j] = 0
        elif manhol[i][j] == 3:                                     # 현재 좌표의 경로가 3이라면 좌우를 지나 갈 수 있으므로
            if 0 <= j + 1 < M and manhol[i][j + 1] in [1,3,6,7]:    # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i, j + 1, T + 1])  # 우
            if 0 <= j - 1 < M and manhol[i][j - 1] in [1,3,4,5]:
                q.append([i, j - 1, T + 1])  # 좌
            manhol[i][j] = 0
        elif manhol[i][j] == 4:                                     # 현재 좌표의 경로가 4라면 상우를 지나 갈 수 있으므로
            if 0 <= i - 1 < N and manhol[i - 1][j] in [1, 2, 5, 6]: # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i - 1, j, T + 1])  # 상
            if 0 <= j + 1 < M and manhol[i][j + 1] in [1, 3, 6, 7]:
                q.append([i, j + 1, T + 1])  # 우
            manhol[i][j] = 0
        elif manhol[i][j] == 5:                                     # 현재 좌표의 경로가 5라면 우하를 지나 갈 수 있으므로
            if 0 <= j + 1 < M and manhol[i][j + 1] in [1,3,6,7]:    # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i, j+1, T + 1])  # 우
            if 0 <= i + 1 < N and manhol[i + 1][j] in [1,2,4,7]:
                q.append([i+1, j, T + 1])  # 하
            manhol[i][j] = 0
        elif manhol[i][j] == 6:                                     # 현재 좌표의 경로가 6이라면 하좌를 지나 갈 수 있으므로
            if 0 <= i + 1 < N and manhol[i + 1][j] in [1, 2, 4, 7]: # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i + 1, j, T + 1])  # 하
            if 0 <= j - 1 < M and manhol[i][j - 1] in [1, 3, 4, 5]:
                q.append([i, j - 1, T + 1])  # 좌
            manhol[i][j] = 0
        elif manhol[i][j] == 7:                                     # 현재 좌표의 경로가 7이라면 상좌를 지나 갈 수 있으므로
            if 0 <= i - 1 < N and manhol[i - 1][j] in [1, 2, 5, 6]: # 위와 같은 방법으로 다음 경로를 탐색하고 추가한다
                q.append([i - 1, j, T + 1])  # 상
            if 0 <= j - 1 < M and manhol[i][j - 1] in [1, 3, 4, 5]:
                q.append([i, j - 1, T + 1])  # 좌
            manhol[i][j] = 0
        elif manhol[i][j] == 0:                                     # 현재 좌표의 경로가 0이라면 통로가 없으므로 패스한다
            pass
    else:                                                           # 이동할 수 있는 통로의 탐색을 마쳤다면
        passage = 0                                                 # 통로의 개수를 저장할 변수를 생성하고
        for a in ans:                                               # 도둑이 지나간 경로를 살펴보며
            if a[2] <= t:                                           # t 시간동안 이동할 수 있는 경로라면
                passage += 1                                        # passage 변수에 추가한다
        print(f'#{p+1}', passage)

