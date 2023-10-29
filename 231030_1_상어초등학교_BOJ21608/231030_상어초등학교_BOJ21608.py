# 상어초등학교_BOJ21608

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 교실의 크기를 input 받고
classroom = [[-1]*N for _ in range(N)]              # 자리 배치를 할 교실 행렬을 생성한다
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]            # 4방향 델타탐색을 위한 리스트를 생성하고
friend = [[] for _ in range(N**2)]                  # 선호하는 친구를 저장할 리스트를 생성한다
for n in range(N**2):                               # 친구의 수를 반복해서
    a, b, c, d, e = map(int, input().split())       # a학생이 선호하는 4명의 학생을 input 받고
    friend[a-1] = [b-1, c-1, d-1, e-1]              # a가 선호하는 학생을 리스트에 담어 저장한다
    seat = []                                       # a를 앉힐 좌석을 저장할 리스트를 생성하고
    max_like = 0                                    # 주변에 선호하는 최대 학생의 수를 저장할 변수를 생성하고
    max_empty = 0                                   # 주변에 비어있는 최대 자리의 수를 저장할 변수를 생성한다
    for i in range(N):                              # 행을 반복하고
        for j in range(N):                          # 열을 반복해서
            if classroom[i][j] == -1:               # i, j 자리에 아직 아무도 앉지 않았을 때
                like = 0                            # i, j 자리에 앉을 때 주변에 좋아하는 학생의 수를 저장할 변수를 생성하고
                empty = 0                           # i, j 자리에 앉을 때 주변에 비어있는 수를 저장할 변수를 생성하고
                for k in range(4):                  # 4방향 델타탐색을 진행해서
                    x = i + dxy[k][0]               # 이동한 곳의 행의 위치를 x에 저장하고
                    y = j + dxy[k][1]               # 이동한 곳의 열의 위츠를 y에 저장해서
                    if 0<=x<N and 0<=y<N:           # 이동한 곳이 교실 내에 위치한다면
                        if classroom[x][y] == -1:   # 이동한 자리가 비어있다면
                            empty += 1              # 빈자리를 하나 추가하고
                        else:                       # 이동한 자리에 학생이 앉아있다면
                            if classroom[x][y] in friend[a-1]:  # 이동한 자리의 학생이 a가 좋아하는 학생이면
                                like += 1           # 좋아하는 학생을 수를 하나 추가한다
                else:                               # 4방향 델타탐색을 마친 후
                    if max_like < like:             # 현재 자리가 저장된 자리보다 좋아하는 학생수가 주변에 더 많다면
                        max_like = like             # 현재 자리의 좋아하는 학생 수를 최대 값으로 저장하고
                        max_empty = empty           # 현재 자리의 빈자리의 수를 최대 값으로 저장한 후
                        seat = []                   # seat 리스트를 초기화하고
                        seat.append([i,j])          # 현재 자리를 append한다
                    elif max_like == like:          # 현재 자리가 저장된 자리와 좋아하는 학생수가 같다면
                        if max_empty < empty:       # 현재 자리가 저장된 자리보다 빈자리가 주변에 더 많다면
                            max_empty = empty       # 현재 자리의 빈자리의 수를 최대 값으로 저장한 후
                            seat = []               # seat 리스트를 초기화하고
                            seat.append([i, j])     # 현재 자리를 append한다
                        elif max_empty == empty:    # 현재 자리가 저장된 자리와 빈자리가 같다면
                            seat.append([i, j])     # seat 리스트에 현재 자리를 append한다
    else:                                           # 모든 자리를 탐색한 후
        classroom[seat[0][0]][seat[0][1]] = a-1     # seat에 저장된 맨 앞 자리에 a 학생을 배정한다
ans = 0                                             # 학생의 만족도를 저장할 변수를 생성하고
score = [0, 1, 10, 100, 1000]                       # 자리의 만족도 점수를 리스트로 저장한다
for i in range(N):                                  # 행을 반복하고
    for j in range(N):                              # 열을 반복해서
        tmp = 0                                     # 주변에 좋아하는 학생의 수를 저장할 변수를 생성하고
        for k in range(4):                          # 4방향 델타탐색을 진행해서
            x = i + dxy[k][0]                       # 이동한 곳의 행의 위치를 x에 저장하고
            y = j + dxy[k][1]                       # 이동한 곳의 열의 위츠를 y에 저장해서
            if 0<=x<N and 0<=y<N:                   # 이동한 곳이 교실 내에 위치한다면
                if classroom[x][y] in friend[classroom[i][j]]:  # 이동한 자리의 학생이 classroom[i][j]이 좋아하는 학생이면
                    tmp += 1                        # tmp를 1 추가한다
        else:                                       # 4방향 델타탐색을 마친 후
            ans += score[tmp]                       # 자리의 만족도를 ans에 더해준다
print(ans)                                          # 학생의 만족도의 총 합을 출력한다