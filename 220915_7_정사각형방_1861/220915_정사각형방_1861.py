# 정사각형방_1861

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                        # 테스트 케이스
for t in range(T):                                                      # 테스트 케이스를 반복할 때
    N = int(input())                                                    # 정사각형 방의 한 변의 길이
    room = []                                                           # 빈 리스트를 만들고
    for n in range(N):                                                  # 정사각형 방의 행의 길이만큼 반복해서
        room.append(list(map(int, input().split())))                    # 각 행마다 input값을 리스트로 받는다

    # 델타 탐색
    dx = [-1, 0, 1, 0]                                                  # 상 우 하 좌
    dy = [0, 1, 0, -1]                                                  # 상 우 하 좌

    maxi = 0                                                            # 최대 이동거리
    start = 0                                                           # 최대 이동 시 시작점

    for i in range(N):                                                  # 정사각형 방의 행을 반복하고
        for j in range(N):                                              # 정사각형 방의 열을 반복해서
            x = i                                                       # 시작점의 행을 x
            y = j                                                       # 시작점의 열을 y 에 저장
            tmp = 1                                                     # 이동거리를 저장할 tmp 생성
            while 1:                                                    # break 될때까지 반복
                for d in range(4):                                      # 델타탐색을 위한 4방향 반복
                    if 0 <= x+dx[d] <= N-1 and 0 <= y+dy[d] <= N-1:     # 델타탐색 범위가 정사각형 방 안일 때
                        if room[x][y] + 1 == room[x+dx[d]][y+dy[d]]:    # 탐색한 방이 탐색 전 방보다 1 크다면
                            x = x+dx[d]                                 # 이동한 방의 행을 x로 저장
                            y = y+dy[d]                                 # 이동한 방의 열을 y로 저장
                            tmp += 1                                    # 이동거리를 1 늘려주고 break
                            break
                else:                                                   # 델타탐색을 해도 조건에 맞는 방이 없다면
                    if tmp > maxi:                                      # 이동거리가 maxi보다 클 때
                        maxi = tmp                                      # maxi에 새로운 최대 이동거리를 저장하고
                        start = room[i][j]                              # 출발점의 요소를 start에 저장한다
                    elif tmp == maxi:                                   # 만약 이동거리와 maxi가 같을 경우엔
                        if start > room[i][j]:                          # 출발점의 요소가 start보다 작다면
                            start = room[i][j]                          # start에 새로운 출발점의 요소를 저장하고
                    break                                               # while문을 break 한다

    print(f'#{t+1}', start, maxi)